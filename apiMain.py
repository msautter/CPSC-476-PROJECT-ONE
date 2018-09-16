from flask import Flask, jsonify, request, make_response
from flask_basicauth import BasicAuth
import json
import sqlite3
import datetime

# sqlite3 auction.db < create.sql
app = Flask(__name__)
# app.config['BASIC_AUTH_USERNAME'] = 'jesus'
# app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)


databaseName = 'databases.db'

def connectDB():
    try:
        global cur
        global conn
        conn = sqlite3.connect(databaseName)
        cur = conn.cursor()
        print("SUCCESS: USER CONNECTED TO DATABASE")
    except:
        return "ERROR: DATABASE OFFLINE"
    
# ********************************************************************
@app.route('/forums', methods=['GET'])
def get_forums():
    responseJSON = []
    connectDB()
    cur.execute("SELECT * FROM forums")
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return jsonify(forumsSQL)
    for forum in forumsSQL:
        responseJSON.append({'id': forum[0], 'title': forum[1], 'creator': forum[2]})    
    responseJSON = jsonify(responseJSON)
    response = make_response(responseJSON)
    response.status_code = 200
    return response
# ********************************************************************

# ********************************************************************
@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    responseJSON = []
    connectDB()
    cur.execute("SELECT * FROM threads WHERE forum_id={}".format(str(forum_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        response = make_response("ERROR: FORUM NOT FOUND")
        response.status_code = 404
        return response
    for thread in threadsSQL:
        responseJSON.append({'id': thread[1], 'title': thread[2], 'creator': thread[3], 'timestamp': thread[4]})
    response = make_response(jsonify(responseJSON))
    response.status_code = 201
    return response
# ********************************************************************

# ********************************************************************
@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
def get_posts(forum_id, thread_id):
    responseJSON = []
    connectDB()
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        response = make_response("ERROR: FORUM NOT FOUND")
        response.status_code = 404
        return reponse
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        response = make_response("ERROR: THREAD NOT FOUND")
        response.status_code = 404
        return reponse
        
    cur.execute("SELECT * FROM posts WHERE forum_id={} AND thread_id={}".format(str(forum_id), str(thread_id)))
    postsSQL = cur.fetchall()
    for post in postsSQL:
        responseJSON.append({'author': post[3], 'text': post[2], 'timestamp': post[4]})
    response = make_response(jsonify(responseJSON))
    response.status_code = 200
    return response
# ********************************************************************


# ********************************************************************
@app.route('/forums', methods=['POST'])
def add_forum():
    connectDB()
    requestJSON = request.get_json(force=True)
    cur.execute("SELECT * FROM forums WHERE forum_name='"+str(requestJSON['name'])+"'")
    forumsSQL = cur.fetchall()
    if forumsSQL != []:
            response = make_response("ERROR: FORUM ALREADY EXISTS")
            response.status_code = 409
            return response
    cur.execute("INSERT INTO forums(forum_name,forum_creator) VALUES (?,?,?)",(str(requestJSON['name']), "marek.sautter", str(datetime.datetime.now())))
    conn.commit()
    cur.execute("SELECT * FROM forums WHERE forum_name={}".format(str(requestJSON['name'])))
    newForum = cur.fetchone()
    response = make_response("SUCCESS: FORUM CREATED")
    response['location'] = '/forums/{}'.format(str(newForum['forum_id']))
    response.status_code = 201
    return response
# ********************************************************************

# ********************************************************************
@app.route('/forums<int:forum_id>', methods=['POST'])
def add_thread(forum_id):
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.datetime.now())
    connectDB()
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        response = make_response("ERROR: FORUM NOT FOUND")
        response.status_code = 404
        return reponse
    cur.execute("INSERT INTO threads(forum_id, thread_creator, thread_title, thread_time) VALUES (?,?,?,?)",(forum_id, "marek.sautter", requestJSON['title'], currentTime))
    conn.commit()
    cur.execute("INSERT INTO posts(forum_id, post_creator, post_text, post_time) VALUES (?,?,?,?)",(forum_id, "marek.sautter", requestJSON['text'], currentTime))
    cur.commit()

    cur.execute("SELECT * FROM threads WHERE thread_name={}".format(str(requestJSON['title'])))
    newThread = cur.fetchone()
    response = make_response("SUCCESS: THREAD CREATED")
    response['location'] = '/forums/{}/{}'.format(str(newThread['forum_id']), str(newThread['thread_id']))
    response.status_code = 201
    return response
# ********************************************************************

# ********************************************************************
@app.route('/forums<int:forum_id>/<int:thread_id>', methods=['POST'])
def add_post(forum_id, thread_id):
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.datetime.now())
    connectDB()
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        response = make_response("ERROR: FORUM NOT FOUND")
        response.status_code = 404
        return response
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        response = make_response("ERROR: FORUM NOT FOUND")
        response.status_code = 404
        return response

    cur.execute("INSERT INTO posts(forum_id, thread_id, post_creator, post_time) VALUES (?,?,?,?,?)",(forum_id, thread_id, "marek.sautter", requestJSON['text'], currentTime))
    conn.commit()
    cur.execute("SELECT * FROM posts WHERE post_name={} AND post_time={}".format(str(requestJSON['text']), str(currentTime)))
    newThread = cur.fetchone()
    response = make_response("SUCCESS: POST CREATED")
    response['location'] = '/forums/{}/{}'.format(str(newThread['forum_id']), str(newThread['thread_id']))
    response.status_code = 201
    return response
# ********************************************************************



# ********************************************************************
@app.route('/users', methods=['POST'])
def add_user():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    connectDB()
    cur.execute("SELECT * FROM users WHERE users_name={}",(str(username)))
    user = cur.fetchall()
    if user != []:
        response = make_response("ERROR: USERNAME ALREADY EXISTS")
        response.status_code = 409
        return response
    cur.execute("INSERT INTO users(users_name, users_pw) VALUES (?,?)",(str(username), str(password)))
    conn.commit()
    response = make_response("SUCCESS: USERNAME CREATED")
    response.status_code = 201
    return response
# ********************************************************************


# ********************************************************************
@app.route('/users', methods=['PUT'])
def change_password():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    connectDB()
    cur.execute("SELECT * FROM users WHERE users_name = '{}'".format(username))
    user = cur.fetchall()
    if user == []:
        response = make_response("ERROR: USER NOT FOUND")
        response.status_code = 404
        return response
    cur.execute("UPDATE users SET users_pw= '{}' WHERE users_name= '{}'".format(password, username))
    conn.commit()
    response = make_response("SUCCESS: PASSWORD CHANGED")
    response.status_code = 201
    return response
# ********************************************************************

if __name__ == '__main__':
    app.run(debug=True)

app.run()
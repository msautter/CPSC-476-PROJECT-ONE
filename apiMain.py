from flask import Flask, jsonify, request, make_response
from flask.cli import AppGroup
from flask_basicauth import BasicAuth
import json
import sqlite3
import datetime
import sys
# sqlite3 auction.db < create.sql
app = Flask(__name__)
basic_auth = BasicAuth(app)
databaseName = 'database.db'

@app.cli.command('init_db')
def init_db():
    try:
        conn = sqlite3.connect(databaseName)
        with app.open_resource('init.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        print("Database file created as {}".format(str(databaseName)))
    except:
        print("Failed to create {}".format(str(databaseName)))
        sys.exit()
app.cli.add_command(init_db)

def connectDB(dbName):
    try:
        conn = sqlite3.connect(dbName)
        print("SUCCESS: CONNECTED TO {}".format(str(dbName)))
        return conn
    except:
        print("ERROR: {} OFFLINE".format(str(dbName)))
        sys.exit()

def checkUser(cur, user_name, pass_word):
    if user_name == '' or pass_word == '':
        return False
    cur.execute("SELECT * FROM users WHERE username='{}'".format(str(user_name)))
    user = cur.fetchone()
    if user[0] == str(user_name) and user[1] == str(pass_word):
        return True
    else:
        return False
            
    
# ********************************************************************
@app.route('/forums', methods=['GET'])
def get_forums():
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM forums")
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return jsonify(forumsSQL)
    for forum in forumsSQL:
        responseJSON.append({'id': forum[0], 'title': forum[1], 'creator': forum[2]})    
    return make_response(jsonify(responseJSON), 200)
# ********************************************************************

# ********************************************************************
@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM threads WHERE forum_id={}".format(str(forum_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        return make_response("FORUM NOT FOUND", 404)
    for thread in threadsSQL:
        responseJSON.append({'id': thread[1], 'title': thread[2], 'creator': thread[4], 'timestamp': thread[5]})
    return make_response(jsonify(responseJSON), 200)
# ********************************************************************

# ********************************************************************
@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
def get_posts(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return make_response("FORUM NOT FOUND", 404)
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        return make_response("THREAD NOT FOUND", 404)
        
    cur.execute("SELECT * FROM posts WHERE forum_id={} AND thread_id={}".format(str(forum_id), str(thread_id)))
    postsSQL = cur.fetchall()
    for post in postsSQL:
        responseJSON.append({'author': post[3], 'text': post[4], 'timestamp': post[5]})
    return make_response(jsonify(responseJSON), )
# ********************************************************************

# ********************************************************************
@app.route('/forums', methods=['POST'])
@basic_auth.required
def add_forum():
    auth = request.authorization
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if login:
        requestJSON = request.get_json(force=True)
        cur.execute("SELECT * FROM forums WHERE forum_name='{}'".format(str(requestJSON['name'])))
        forumsSQL = cur.fetchall()
        if forumsSQL != []:
                return make_response("FORUM ALREADY EXISTS", 409)
        cur.execute("INSERT INTO forums(forum_name,forum_creator) VALUES (?,?,?)",(str(requestJSON['name']), str(auth.username), str(datetime.datetime.now())))
        conn.commit()
        cur.execute("SELECT * FROM forums WHERE forum_name={}".format(str(requestJSON['name'])))
        newForum = cur.fetchone()
        return make_response("SUCCESS: FORUM CREATED", 201, {"location" : '/forums/' + str(newForum['forum_id'])})
    return []
# ********************************************************************

# ********************************************************************
@app.route('/forums<int:forum_id>', methods=['POST'])
@basic_auth.required
def add_thread(forum_id):
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.datetime.now())
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if not login['result']: return login["message"]
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return make_response("ERROR: FORUM NOT FOUND", 404)
    cur.execute("INSERT INTO threads(forum_id, thread_creator, thread_title, thread_time) VALUES (?,?,?,?)",(forum_id, str(auth.username), requestJSON['title'], currentTime))
    conn.commit()
    cur.commit()
    cur.execute("INSERT INTO posts(forum_id, post_creator, post_text, post_time) VALUES (?,?,?,?)",(forum_id, str(auth.username), requestJSON['text'], currentTime))
    conn.commit()
    cur.commit()

    cur.execute("SELECT * FROM threads WHERE thread_name={}".format(str(requestJSON['title'])))
    newThread = cur.fetchone()
    return make_response("SUCCESS: THREAD CREATED", 201, {"location" : '/forums/{}/{}'.format(str(newThread['forum_id']), str(newThread['thread_id']))})
# ********************************************************************

# ********************************************************************
@app.route('/forums<int:forum_id>/<int:thread_id>', methods=['POST'])
@basic_auth.required
def add_post(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.datetime.now())

    login = checkUser(cur, auth.username, auth.password)
    if not login['result']: return login["message"]
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return make_response("ERROR: FORUM NOT FOUND", 404)
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        return make_response("ERROR: THREAD NOT FOUND", 404)
    cur.execute("INSERT INTO posts(forum_id, thread_id, post_creator, post_time) VALUES (?,?,?,?,?)",(forum_id, thread_id, str(auth.username), requestJSON['text'], currentTime))
    conn.commit()
    cur.execute("SELECT * FROM posts WHERE post_name={} AND post_time={}".format(str(requestJSON['text']), str(currentTime)))
    newThread = cur.fetchone()
    return make_response("SUCCESS: POST CREATED", 201, {"location" : '/forums/{}/{}'.format(str(newThread['forum_id']), str(newThread['thread_id']))})
# ********************************************************************

# ********************************************************************
@app.route('/users', methods=['POST'])
def add_user():
    requestJSON = request.get_json(force=True)
    username = requestJSON['username']
    password = requestJSON['password']
    conn = connectDB(databaseName)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username={}",(str(username)))
    user = cur.fetchall()
    if user != []:
        return make_response("CONFLICT: USER EXISTS", 409)
    cur.execute("INSERT INTO users(username, password) VALUES (?,?)",(str(username), str(password)))
    conn.commit()
    return make_response("SUCCESS: USER CREATED", 201)
# ********************************************************************


# ********************************************************************
@app.route('/users', methods=['PUT'])
@basic_auth.required
def change_password():
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    username = requestJSON['username']
    password = requestJSON['password']
    if requestJSON['username'] != auth.username:
        return make_response("CONFLICT: USERNAME NOT EQUAL", 409)
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if not login['result']: return login["message"]
    cur.execute("SELECT * FROM users WHERE username = '{}'".format(username))
    user = cur.fetchall()
    if user == []:
        return make_response("ERROR: USER NOT FOUND", 404)
    cur.execute("UPDATE users SET password= '{}' WHERE username= '{}'".format(password, username))
    conn.commit()
    return make_response("SUCCESS: PASSWORD CHANGED", 200)
# ********************************************************************

if __name__ == '__main__':
    app.run(debug=True)

app.run()
from flask import Flask, jsonify, request, make_response
from flask.cli import AppGroup
from flask_basicauth import BasicAuth
import json
import sqlite3
from datetime import datetime
import sys
# sqlite3 database.db < init.sql
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
basic_auth = BasicAuth(app)
databaseName = 'database.db'

# HELPER FUNCTIONS --------------------------------------------------
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
    cur.execute("SELECT * FROM Users WHERE username='{}'".format(str(user_name)))
    user = cur.fetchone()
    if user == None:
        print("Couldn't find")
        return False
    elif user[0] == str(user_name) and user[1] == str(pass_word):
        return True
    return False

def fixDate(my_date):
    new_date = datetime.strptime(my_date,'%Y-%m-%d %H:%M:%S.%f')
    return new_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

def createDate():
    new_date = datetime.now()
    return new_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

# HELPER FUNCTIONS ---------------------------------------------------

# DONE ---------------------------------------------------------- DONE        
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
        responseJSON.append({'id': forum[0], 'name': forum[1], 'creator': forum[2]})    
    return make_response(jsonify(responseJSON), 200)
# ********************************************************************
# DONE ---------------------------------------------------------- DONE     


# The timestamp for a thread is the timestamp for the most recent post to that thread <>
# The creator for a thread is the author of its first post <>
# Threads are listed in reverse chronological order <>
# ********************************************************************
@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM threads WHERE forum_id={}".format(str(forum_id)))
    # cur.execute("SELECT * FROM Threads INNER JOIN Forums ON Threads.forum_id = Forums.forum_id AND Threads.forum_id = {}".format(str(forum_id)))
    threadsSQL = cur.fetchall()
    for post in threadsSQL:
        cur.execute("SELECT * FROM posts WHERE forum_id='{}' AND thread_id ='{}'".format( str(forum_id), str(post[1])))
        postsSQL = cur.fetchall()
        print(postsSQL)
    # print(str(threadsSQL))
    # print(str(postsSQL))
    if threadsSQL == []:
        return make_response("NOT FOUND", 404)
    for thread in threadsSQL:
        responseJSON.append({'id': thread[1], 'title': thread[2], 'creator': thread[4], 'timestamp': fixDate(thread[5])})
    return make_response(jsonify(responseJSON), 200)
# ********************************************************************




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
def get_posts(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return make_response("NOT FOUND", 404)
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        return make_response("NOT FOUND", 404)
        
    cur.execute("SELECT * FROM posts WHERE forum_id={} AND thread_id={}".format(str(forum_id), str(thread_id)))
    postsSQL = cur.fetchall()
    for post in postsSQL:
        responseJSON.append({'author': post[3], 'text': post[4], 'timestamp': fixDate(post[5])})
    # newlist = sorted(responseJSON, key=lambda k: k['timestamp'], reverse=True) 
    # print(newlist)
    return make_response(jsonify(responseJSON), 200)
# ********************************************************************
# DONE  --------------------------------------------------------  DONE




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/forums', methods=['POST'])
def add_forum():
    auth = request.authorization
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if login:
        requestJSON = request.get_json(force=True)
        cur.execute("SELECT * FROM forums WHERE forum_title='{}'".format(str(requestJSON['name'])))
        forumsSQL = cur.fetchall()
        if forumsSQL != []:
            return make_response("FORUM ALREADY EXISTS", 409)
        cur.execute("INSERT INTO forums(forum_title,creator) VALUES (?,?)",(str(requestJSON['name']), str(auth.username)))
        conn.commit()
        cur.execute("SELECT * FROM forums WHERE forum_title='{}'".format(str(requestJSON['name'])))
        newForum = cur.fetchone()
        return make_response("SUCCESS: FORUM CREATED", 201, {"location" : '/forums/' + str(newForum[0])})
    return "ERROR: UNSUCCESSFUL LOGIN"
# ********************************************************************
# DONE  --------------------------------------------------------  DONE




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/forums/<int:forum_id>', methods=['POST'])
def add_thread(forum_id):
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.now())
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if login:
        cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
        forumsSQL = cur.fetchall()
        if forumsSQL == []:
            return make_response("NOT FOUND", 404)
        cur.execute("INSERT INTO threads(forum_id, creator, thread_title, thread_text, thread_time) VALUES (?,?,?,?,?)",(forum_id, str(auth.username), requestJSON['title'], requestJSON['text'], currentTime))
        conn.commit()
        cur.execute("SELECT * FROM threads WHERE thread_title='{}'".format(str(requestJSON['title'])))
        newThread = cur.fetchone()
        cur.execute("INSERT INTO posts(forum_id, thread_id, author, post_text, post_time) VALUES (?,?,?,?,?)",(forum_id, str(newThread[1]), str(auth.username), requestJSON['text'], currentTime))
        conn.commit()
        return make_response("SUCCESS: THREAD CREATED", 201, {"location" : '/forums/{}/{}'.format(str(newThread[0]), str(newThread[1]))})
    else:
        return make_response("ERROR: LOGIN UNSUCCESSFUL")
# ********************************************************************
# DONE  --------------------------------------------------------  DONE




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['POST'])
def add_post(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.now())
    login = checkUser(cur, auth.username, auth.password)
    if login:
        cur.execute("SELECT * FROM forums WHERE forum_id='{}'".format(str(forum_id)))
        forumsSQL = cur.fetchall()
        if forumsSQL == []:
            return make_response("NOT FOUND", 404)
        cur.execute("SELECT * FROM threads WHERE thread_id='{}'".format(str(thread_id)))
        threadsSQL = cur.fetchall()
        if threadsSQL == []:
            return make_response(" FOUND", 404)
        cur.execute("INSERT INTO posts(forum_id, thread_id, author, post_text, post_time) VALUES (?,?,?,?,?)",(forum_id, thread_id, str(auth.username), requestJSON['text'], currentTime))
        conn.commit()
        return make_response("SUCCESS: POST CREATED", 201)
    else:
        return make_response("ERROR: LOGIN UNSUCCESSFUL")
# ********************************************************************
# DONE  --------------------------------------------------------  DONE




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/users', methods=['POST'])
def add_user():
    requestJSON = request.json
    username = requestJSON['username']
    password = requestJSON['password']
    conn = connectDB(databaseName)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username='{}'".format(str(username)))
    user = cur.fetchone()
    if user != None:
        return make_response("CONFLICT: USER EXISTS", 409)
    cur.execute("INSERT INTO users(username, password) VALUES (?,?)",(str(username), str(password)))
    conn.commit()
    conn.close()
    return make_response("SUCCESS: USER CREATED", 201)
# ********************************************************************
# DONE  --------------------------------------------------------  DONE




# DONE  --------------------------------------------------------  DONE
# ********************************************************************
@app.route('/users', methods=['PUT'])
def change_password():
    auth = request.authorization
    requestJSON = request.json
    username = requestJSON['username']
    password = requestJSON['password']
    if requestJSON['username'] != auth.username:
        return make_response("CONFLICT: USERNAME NOT EQUAL", 409)
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username, auth.password)
    if login:
        cur.execute("SELECT * FROM users WHERE username = '{}'".format(username))
        user = cur.fetchall()
        if user == []:
            return make_response("NOT FOUND", 404)
        cur.execute("UPDATE users SET password= '{}' WHERE username= '{}'".format(password, username))
        conn.commit()
        return make_response("SUCCESS: PASSWORD CHANGED", 200)
    else: 
        return make_response("ERROR: Unsuccessful Login")
# ********************************************************************
# DONE  --------------------------------------------------------  DONE





if __name__ == '__main__':
    app.run(debug=True)

app.run()
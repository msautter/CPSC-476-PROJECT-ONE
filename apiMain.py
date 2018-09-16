from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
import json
import sqlite3
import datetime

# sqlite3 auction.db < create.sql
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'jesus'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)


databaseName = 'databases.db'
responseJSON = []
reponse = ""

def connectDB():
    try:
        global cur
        global conn
        conn = sqlite3.connect(databaseName)
        cur = conn.cursor()
    except:
        print("Failed to connect to " + databaseName)
    
# ********************************************************************
@app.route('/forums', methods=['GET'])
def get_forums():
    responseJSON = []
    connectDB()
    cur.execute("SELECT * FROM forums")
    sqlForums = cur.fetchall()
    for forum in sqlForums:
        responseJSON.append({'id': forum[0], 'title': forum[1], 'creator': forum[2]})    
    return jsonify(responseJSON)
# ********************************************************************


# ********************************************************************
@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    reponseJSON = []
    connectDB()
    cur.execute("SELECT * FROM threads WHERE forum_id={}".format(str(forum_id)))
    sqlThreads = cur.fetchall()
    for thread in sqlThreads:
        responseJSON.append({'id': thread[1], 'title': thread[2], 'creator': thread[4], 'timestamp': thread[5]})
    return jsonify(responseJSON)
# ********************************************************************


# ********************************************************************
@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
def get_posts(forum_id, thread_id):
    responseJSON = []
    connectDB()
    cur.execute("SELECT * FROM posts WHERE forum_id={} AND thread_id={}".format(str(forum_id), str(thread_id)))
    postsSQL = cur.fetchall()
    for post in postsSQL:
        responseJSON.append({'author': post[4], 'text': post[3], 'timestamp': post[5]})
    return jsonify(responseJSON)
# ********************************************************************


# ********************************************************************
@app.route('/forums', methods=['POST'])
def add_forum():
    connectDB()
    requestJSON = request.get_json(force=True)
    cur.execute("SELECT * FROM forums WHERE forum_name='"+str(requestJSON['name'])+"'")
    forums = cur.fetchall()
    if forums != []:
        print(requestJSON['name'])
        cur.execute("INSERT INTO forums(forum_name,forum_creator) VALUES (?,?)",(str(requestJSON['name']), "marek.sautter"))
        conn.commit()
        return "MADE IT"
    conn.commit()
    return "TEST"
# ********************************************************************


# ********************************************************************
@app.route('/users', methods=['POST'])
def add_user():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    connectDB()
    cur.execute("INSERT INTO users(users_name, users_pw) VALUES (?,?)",(str(username), str(password)))
    conn.commit()
    return  "Hello"
# ********************************************************************


# ********************************************************************
@app.route('/users', methods=['PUT'])
def change_password():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    print(str(username))
    print(str(password))
    connectDB()
    cur.execute("SELECT * FROM users WHERE users_name = '{}'".format(username))
    dbUser = cur.fetchall()
    if dbUser == []:
        return "User not found"
    cur.execute("UPDATE users SET users_pw= '{}' WHERE users_name= '{}'".format(password, username))
    conn.commit()
    return  "Hello"
# ********************************************************************

if __name__ == '__main__':
    app.run(debug=True)

app.run()
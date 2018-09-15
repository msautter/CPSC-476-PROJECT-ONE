from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
databaseName = 'databases.db'



@app.route('/forums', methods=['GET'])
def get_forums():
    try:
        conn = sqlite3.connect(databaseName)
        print('Successfully connect to '+ databaseName)
        cur = conn.cursor()
    except:
        print("Failed to connect to " + databaseName)
    cur.execute("SELECT * FROM forums")
    forums = cur.fetchall()
    # conn.close()
    # cur.close()
    return jsonify(forums)

@app.route('/forums', methods=['POST'])
def add_forum():
    requestJson = request.get_json(force=True)
    
    return "TEST"

@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    try:
        conn = sqlite3.connect(databaseName)
        print('Successfully connect to '+ databaseName)
        cur = conn.cursor()
    except:
        print("Failed to connect to " + databaseName)
    cur.execute("SELECT * FROM threads WHERE forum_id=" + str(forum_id))
    threads = cur.fetchall()
    # conn.close()
    # cur.close()
    return jsonify(threads)

@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
def get_posts(forum_id, thread_id):
    try:
        conn = sqlite3.connect(databaseName)
        print('Successfully connect to '+ databaseName)
        cur = conn.cursor()
    except:
        print("Failed to connect to " + databaseName)
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    thread = cur.fetchone()
    cur.execute("SELECT * FROM posts WHERE forum_id={} AND thread_id={}".format(str(forum_id), str(thread_id)))
    posts = cur.fetchall()
    # conn.close()
    # cur.close()
    return jsonify(thread, posts)

@app.route('/users', methods=['POST'])
def add_user():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    return  "Hello"

@app.route('/users', methods=['PUT'])
def change_password():
    requestJson = request.get_json(force=True)
    username = requestJson['username']
    password = requestJson['password']
    return  "Hello"


if __name__ == '__main__':
    app.run(debug=True)

app.run()
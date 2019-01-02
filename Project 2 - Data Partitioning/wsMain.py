# NAME: Marek Sautter
# PROF: Kenytt Avery
# CLSS: CPSC 476
# DATE: 31 October
# PROJ: 2 - Sharding Flask Forum API

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import json, sqlite3, sys
from flask import Flask, jsonify, request, make_response
from flask.cli import AppGroup
from flask_basicauth import BasicAuth
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
basic_auth = BasicAuth(app)
databaseName = 'tables.db'
# < HELPER FUNCTIONS --------------------------------------------------
@app.cli.command('init_db')
def init_db():            
    try:
        database = sqlite3.connect(databaseName)
        with app.open_resource('init.sql', mode='r') as f:
            database.cursor().executescript(f.read())
        database.commit()
        print("DATABASES CREATED")
    except:
        sys.exit("DATABASES FAILED")
    finally:
        database.close()
app.cli.add_command(init_db)

def connect_post(post):
    post = post % 3
    post = 'post_{}.db'.format(post)
    try:
        postDb = sqlite3.connect(post)
        print("Connected to: {}".format(post))
    except:
        exit("Unable to connect to: {}".format(post))
    return postDb

def gen_guid():
    sqlite3.register_converter('GUID', lambda b: uuid.UUID(bytes_le=b))
    sqlite3.register_adapter(uuid.UUID, lambda u: buffer(u.bytes_le))
    GUID = uuid.uuid4()
    return GUID

def connectDB(dbName):  
    # Connects to database and returns the connection, if database is offline, program exits
    try:
        conn = sqlite3.connect(dbName)
        print("SUCCESS: CONNECTED TO {}".format(str(dbName)))
        return conn
    except:
        print("ERROR: {} OFFLINE".format(str(dbName)))
        sys.exit()

def checkUser(cur, user_name, pass_word):
    # Simple log in check for the authorization username and password
    if user_name == '' or pass_word == '':
        return False
    cur.execute("SELECT * FROM Users WHERE username='{}'".format(str(user_name)))
    user = cur.fetchone()
    if user == None:
        return False
    elif user[0] == str(user_name) and user[1] == str(pass_word):
        return True
    return False

def fixDate(my_date):   
    # Reads the raw string date, creates date object, and returns correct format
    new_date = datetime.strptime(my_date,'%Y-%m-%d %H:%M:%S.%f')
    return new_date.strftime('%a, %d %b %Y %H:%M:%S GMT')

def compareDates(prevDate, nextDate):
    # Finds the most recent date, used for finding most recent date out of posts
    prevDate = datetime.strptime(str(prevDate),'%Y-%m-%d %H:%M:%S.%f')
    nextDate = datetime.strptime(str(nextDate),'%Y-%m-%d %H:%M:%S.%f')
    if prevDate <= nextDate:
        return nextDate
    return prevDate 

# HELPER FUNCTIONS />---------------------------------------------------
       
@app.route('/forums', methods=['GET'])
def get_forums():
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM forums")
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        # Returns an empty array if no forums have been created
        conn.close()
        return make_response(jsonify(forumsSQL), 200)
    for forum in forumsSQL:
        responseJSON.append({'id': forum[0], 'name': forum[1], 'creator': forum[2]}) 
    conn.close()   
    return make_response(jsonify(responseJSON), 200)
    
@app.route('/forums', methods=['POST'])
# @basic_auth.required 
def add_forum():
    auth = request.authorization
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username.lower(), auth.password)
    if login:
        requestJSON = request.get_json(force=True)
        cur.execute("SELECT * FROM forums WHERE forum_title='{}'".format(str(requestJSON['name'])))
        forumsSQL = cur.fetchall()
        if forumsSQL != []:
            conn.close()
            return make_response("FORUM ALREADY EXISTS", 409)
        cur.execute("INSERT INTO forums(forum_title,creator) VALUES (?,?)",(str(requestJSON['name']), str(auth.username)))
        conn.commit()
        cur.execute("SELECT * FROM forums WHERE forum_title='{}'".format(str(requestJSON['name'])))
        newForum = cur.fetchone()
        conn.close()
        # Location header field set to /forums/<forum_id> for new id
        return make_response("SUCCESS: FORUM CREATED", 201, {"location" : '/forums/' + str(newForum[0])})
    conn.close()
    return make_response("ERROR: Unsuccessful Login / Unauthorized", 401)

@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []
    cur.execute("SELECT * FROM threads WHERE forum_id={}".format(str(forum_id)))
    threadsSQL = cur.fetchall()
    if threadsSQL == []:
        return make_response("NOT FOUND", 404)

    # I know this is probably a dumb way to get the most recent date but I'm not a
    # Database genius so I'm just gonna stick with my poorly optimized nested for loop
    for thread in threadsSQL:
        thread_key = thread[2]
        thread_id = thread[1]
        postCursor = connect_post(thread_id).cursor()
        postCursor.execute('''SELECT * FROM Posts WHERE post_key = ?''',(thread_key, ))
        postList = cur.fetchall()
        if postList == []:
            responseJSON.append({'id': thread[1], 'title': thread[3], 'creator': thread[5], 'timestamp': fixDate(str(thread[6]))})
        else:
            newestDate = "2000-01-01 01:00:00.000000"
            for post in postList:
                newestDate = compareDates(newestDate, str(post[3]))
            responseJSON.append({'id': thread[1], 'title': thread[3], 'creator': thread[5], 'timestamp': fixDate(str(newestDate))})
    conn.close()
    # Threads are listed in reverse chronological order (by date? or by id? I'm gonna go with date
    responseJSON = sorted(responseJSON, key=lambda k: k['timestamp'], reverse=True) 
    return make_response(jsonify(responseJSON), 200)

@app.route('/forums/<int:forum_id>', methods=['POST'])
# @basic_auth.required 
def add_thread(forum_id):
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.now())
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username.lower(), auth.password)
    if login:
        cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
        forumsSQL = cur.fetchall()
        if forumsSQL == []:
            conn.close()
            return make_response("NOT FOUND", 404)
        # TO GET THE NEWEST THREAD ID SINCE AUTO INCREMENT WASNT WORKING IN SQL
        cur.execute("SELECT * FROM threads")
        tempThreads = cur.fetchall()
        highestThreadNum = -1
        for thread in tempThreads:
            if highestThreadNum < thread[1]:
                highestThreadNum = thread[1]
        highestThreadNum+=1

        # GENERATE NEW THREAD ID
        guid = gen_guid()
        cur.execute("INSERT INTO threads(forum_id, thread_id, thread_key, creator, thread_title, thread_text, thread_time) VALUES (?,?,?,?,?,?,?)",(forum_id, highestThreadNum, str(guid), str(auth.username), requestJSON['title'], requestJSON['text'], currentTime))
        conn.commit()
        cur.execute("SELECT * FROM threads WHERE thread_title='{}'".format(str(requestJSON['title'])))
        newThread = cur.fetchone()
        conn.close()
        return make_response("SUCCESS: THREAD CREATED", 201, {"location" : '/forums/{}/{}'.format(str(newThread[0]), str(newThread[1]))})
    conn.close()
    return make_response("ERROR: Unsuccessful Login / Unauthorized", 401)

@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['GET'])
# @basic_auth.required 
def get_posts(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    responseJSON = []

    # DUMB WAY OF CHECKING TO MAKE SURE THE THREAD/FORUM EXISTS
    cur.execute("SELECT * FROM forums WHERE forum_id={}".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        conn.close()
        return make_response("NOT FOUND", 404)
    cur.execute("SELECT * FROM threads WHERE thread_id={}".format(str(thread_id)))
    threadsSQL = cur.fetchone()
    if threadsSQL == None:
        conn.close()
        return make_response("NOT FOUND", 404)
    else:
        # Get the thread text because its technically the first post
        responseJSON.append({'author':threadsSQL[5], 'text': threadsSQL[4], 'timestamp': fixDate(threadsSQL[6])})
        post_key = threadsSQL[2]
        postCursor = connect_post(thread_id).cursor()
        postCursor.execute('''SELECT * FROM Posts WHERE post_key = ?''',(post_key, ))
        postsSQL = postCursor.fetchall()
        if postsSQL == []:
            return make_response(jsonify(responseJSON), 200)
        for post in postsSQL:
            responseJSON.append({'author': post[1], 'text': post[2], 'timestamp': fixDate(post[3])})
        conn.close()
        return make_response(jsonify(responseJSON), 200)

@app.route('/forums/<int:forum_id>/<int:thread_id>', methods=['POST'])
# @basic_auth.required 
def add_post(forum_id, thread_id):
    conn = connectDB(databaseName)
    cur = conn.cursor()
    auth = request.authorization
    requestJSON = request.get_json(force=True)
    currentTime = str(datetime.now())
    login = checkUser(cur, auth.username.lower(), auth.password)
    if login:
        cur.execute("SELECT * FROM forums WHERE forum_id='{}'".format(str(forum_id)))
        forumsSQL = cur.fetchall()
        if forumsSQL == []:
            conn.close()
            return make_response("NOT FOUND", 404)
        cur.execute("SELECT * FROM threads WHERE thread_id='{}'".format(str(thread_id)))
        threadsSQL = cur.fetchall()
        if threadsSQL == []:
            conn.close()
            return make_response("NOT FOUND", 404)
        cur.execute("SELECT * FROM Threads WHERE thread_id = ?", (thread_id,))
        post_key = cur.fetchone()[2]
        print(post_key)
        postCon = connect_post(thread_id)
        postCursor = postCon.cursor()
        postCursor.execute("INSERT INTO Posts(post_key, author, post_text, post_time) VALUES (?,?,?,?)",(post_key, str(auth.username), requestJSON['text'], currentTime))
        postCon.commit()
        conn.commit()
        postCon.close()
        conn.close()
        return make_response("SUCCESS: POST CREATED", 201)
    conn.close()
    return make_response("ERROR: Unsuccessful Login / Unauthorized", 401)

@app.route('/users', methods=['POST'])
def add_user():
    requestJSON = request.json
    username = requestJSON['username'].lower()
    password = requestJSON['password']
    conn = connectDB(databaseName)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username='{}'".format(str(username)))
    user = cur.fetchone()
    if user != None:
        conn.close()
        return make_response("CONFLICT: USER EXISTS", 409)
    cur.execute("INSERT INTO users(username, password) VALUES (?,?)",(str(username), str(password)))
    conn.commit()
    conn.close()
    return make_response("SUCCESS: USER CREATED", 201)

@app.route('/users', methods=['PUT'])
# @basic_auth.required   
def change_password():
    auth = request.authorization
    requestJSON = request.json
    username = requestJSON['username'].lower()
    password = requestJSON['password']
    if username != auth.username.lower():
        return make_response("CONFLICT: USERNAME NOT EQUAL", 409)
    conn = connectDB(databaseName)
    cur = conn.cursor()
    login = checkUser(cur, auth.username.lower(), auth.password)
    if login:
        cur.execute("SELECT * FROM users WHERE username = '{}'".format(str(username)))
        user = cur.fetchall()
        if user == []:
            conn.close()
            return make_response("NOT FOUND", 404)
        cur.execute("UPDATE users SET password= '{}' WHERE username= '{}'".format(str(password), str(username)))
        conn.commit()
        conn.close()
        return make_response("SUCCESS: PASSWORD CHANGED", 200)
    conn.close()
    return make_response("ERROR: Unsuccessful Login / Unauthorized", 401)

if __name__ == '__main__':
    app.run(debug=True)

app.run()
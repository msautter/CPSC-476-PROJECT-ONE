from flask import Flask, jsonify, request, make_response
import json
import sqlite3
import datetime


app = Flask(__name__)
databaseName = "databases.db"

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>You are logged in</h1>'
    return make_response("Could not verify!", 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


    try:
        conn = sqlite3.connect(databaseName)
        print('Successfully connected to '+ databaseName)
        cur = conn.cursor()
    except:
        print("Failed to connect to " + databaseName)
    cur.execute("SELECT * FROM users WHERE users_name="+str(request.authorization.username))
    user = cur.fetchall()
    print(str(user))
    if user == []:
        return make_response("Username Not Found", 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    elif request.authorization.password == user['users_pw']:
        return '<h1>You are logged in</h1>'
    return "Something went wrong"

if __name__ == '__main__':
    app.run(debug=True)

app.run()
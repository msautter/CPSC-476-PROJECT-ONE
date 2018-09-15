from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
databaseName = 'databases.db'
try:
    conn = sqlite3.connect(databaseName)
    print('Successfully connect to '+ databaseName)
except:
    print("Failed to connect to " + databaseName)


@app.route('/forums', methods=['GET'])
def get_forums():
    return "TEST"

@app.route('/forums', methods=['POST'])
def add_forum():
    return "TEST"

@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_threads(forum_id):
    return "TEST"


if __name__ == '__main__':
    app.run(debug=True)

app.run()
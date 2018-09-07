from flask import Flask, jsonify

app = Flask(__name__)

sampleForums = [
    {
        'id': 1,
        'name': "redis",
        'creator': "bob"
    },
    {
        'id': 2,
        'name': "mongodb",
        'creator': "alice"
    }
]

sampleThreads = [
    {
        "id": 1,
        "title": "Does anyone know how to start Redis?",
        "creator": 'bob',
        "timestamp": "Wed, 05 Sep 2018 16:22:29 GMT"
    },
    {
        "id": 2,
        "title": "Has anyone heard of Edis?",
        "creator": "charlie",
        "timestamp": "Tue, 04 Sep 2018 13:18:43 GMT"
    }
]

sampleDiscussion = [
    {
        "author": "bob",
        "text": "I'm trying to connect to MongoDB, but it doesn't seem to be running.",
        "timestamp": "Tue, 04 Sep 2018 15:42:28 GMT"
    },
    {
        "author": "alice",
        "text": "Ummm… maybe 'sudo service start mongodb'?",
        "timestamp": "Tue, 04 Sep 2018 15:45:36 GMT"
    }
]


@app.route('/forums', methods=['GET'])
def get_forums():
    return jsonify({sampleForums})

if __name__ == '__main__':
    app.run(debug=True)

app.run()
from flask import Flask, jsonify

app = Flask(__name__)

sampleForums = [
    {
        'id': 1,
        'name': "Python",
        'creator': "Marek"
    },
    {
        'id': 2,
        'name': "Javascript",
        'creator': "Jessica"
    }
]

sampleThreads = [
    {
        "id": 1.1,
        "title": "What's everyone's favorite thing about Python?",
        "creator": 'Tony',
        "timestamp": "Wed, 05 Sep 2018 16:22:29 GMT"
    },
    {
        "id": 1.2,
        "title": "Any good python libraries I should try?",
        "creator": "Charlie",
        "timestamp": "Tue, 04 Sep 2018 13:18:43 GMT"
    },
    {
        "id": 2.1,
        "title": "Why does everyone like JavaScript?",
        "creator": 'Tom',
        "timestamp": "Wed, 05 Sep 2018 13:22:29 GMT"
    },
    {
        "id": 2.2,
        "title": "JavaScript should be the universal language. Change my mind.",
        "creator": "Linus",
        "timestamp": "Tue, 04 Sep 2018 05:21:53 GMT"
    },
    {
        "id": 2.3,
        "title": "JavaScript tips and tricks.",
        "creator": "Sally",
        "timestamp": "Tue, 04 Sep 2018 09:18:43 GMT"
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
    return jsonify({"sampleForums": sampleForums})

@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_Threads(forum_id):
    
    return jsonify({"sampleThreads": sampleThreads})

if __name__ == '__main__':
    app.run(debug=True)

app.run()
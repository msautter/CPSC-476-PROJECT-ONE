CPSC-476-PROJECT-ONE

This is a simple forum built using python and flask. It relies on API calls and has no front end (for now).

The sample database is populated with televangelists discussing their opinions on today's programming languages.

Here are some examples for interacting with the forum:

1. VIEW ALL FORUMS
API_CALL:   curl http://127.0.0.1:5000/forums
RESPONSE:   ['{"id": 1, "name": "Python", "creator": "marek.sautter"}', '{"id": 2, "name": "Java", "creator": "jesus.christ"}', '{"id": 3, "name": "C++", "creator": "ray.comfort"}']

2. POST A NEW FORUM
API_CALL:   curl -d '{"name":"Python"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/forums
RESPONSE:   HTTP 201 Created

3. GET THREADS FROM A FORUM
API_CALL:   curl http://127.0.0.1:5000/forums/1
RESPONSE:   [ [ 1, 1, "Python is the future of programming!", "I just love Python so much and I wanted to start a thread to share my love", "martin.luther", "2018-09-14 15:00:47.128324" ], [ 1, 2, "How do you avoid creating 'spaghetti-code'?", "Everytime I start something in Python it just ends up being a huge mess. What are the best practices for OOP principles in Python?", "billy.graham", "2018-09-14 15:03:17.245418" ] ]



import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#                METHOD:    GET
#                   URL:    /forums/<forum_id>
#                ACTION:    List threads in the specified forum
#       REQUEST PAYLOAD:    N/A
#   SUCCESSFUL RESPONSE:    HTTP 200 OK
#                           [
#                               {
#                                   "id" : 1,
#                                   "title" : "Does anyone know how to start Redis?",
#                                   "creator" : "bob",
#                                   "timestamp" : "Wed, 05 Sep 2018 16:22:29 GMT"
#                               },
#                               {
#                                   "id" : 2,
#                                   "title" : "Has anyone heard of Edis?",
#                                   "creator" : "charlie",
#                                   "timestamp" : "Tue, 04 Sep 2018 13:18:43 GMT"
#                               },  
#                           ]
#        ERROR RESPONSE:    HTTP 200 OK
#      AUTHENTIFICATION:    NO
#                 NOTES:    The timestamp for a thread is the timestamp to the most recent post to that thread
#                           The creator for a thread is the author of its first post
#                           Threads are listed in reverse chronological order
@app.route('/forums/<forum_id>', methods=['GET'])
def getThreads():
    return "<h1>Thread</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    POST 
#                   URL:    /forums/<forum_id> 
#                ACTION:    Create a new thread in the specified forum 
#       REQUEST PAYLOAD:    
#                           {
#                               "title" : "Does anyone know how to start MongoDB?",
#                               "text" : "I'm trying to connect to MongoDB, but it doesn't seem to be running."  
#                           }
#   SUCCESSFUL RESPONSE:    HTTP 201 Created
#                           Location header field set to /forums/<forum_id>/<thread_id> for new thread
#        ERROR RESPONSE:    HTTP 404 Not Found 
#      AUTHENTIFICATION:    YES
#                 NOTES:    The "text" field becomes the first post to the thread. 
#                           The first post's author is the current authenticated user.
@app.route('/forums/<forum_id>', methods=['POST'])
def postThread():
    return "<h1>Thread</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    GET
#                   URL:    /forums/<forum_id>/<thread_id> 
#                ACTION:    Lists posts to the specified thread 
#       REQUEST PAYLOAD:    N/A 
#   SUCCESSFUL RESPONSE:    HTTP 200 OK 
#                           [
#                               {
#                                   "author": "bob",
#                                   "text": "I'm trying to connect to MongoDB, but it doesn't seem to be running.",
#                                   "timestamp”: "Tue, 04 Sep 2018 15:42:28 GMT"
#                               },
#                               {
#                                   "author": "alice",
#                                   "text": "Ummm… maybe 'sudo service start mongodb'?",
#                                   "timestamp”: "Tue, 04 Sep 2018 15:45:36 GMT"
#                               }
#                           ]
#        ERROR RESPONSE:    HTTP 404 Not Found
#      AUTHENTIFICATION:    No
#                 NOTES:    Posts are listed in chronological order
@app.route('/forums/<forum_id>/<thread_id>', methods=['GET'])
def getPosts():
    return "<h1>Thread</h>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    POST 
#                   URL:    /forums/<forum_id>/<thread_id> 
#                ACTION:    Add a new post to the specified thread 
#       REQUEST PAYLOAD:    
#                           {
#                               "text": "Derp."
#                           }
#   SUCCESSFUL RESPONSE:    HTTP 201 Created
#        ERROR RESPONSE:    HTTP 404 Not Found
#      AUTHENTIFICATION:    YES
#                 NOTES:    The post's author is the current authenticated user
@app.route('/forums/<forum_id>/<thread_id>', methods=['POST'])
def postPost():
    return "<h1>THREAD</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
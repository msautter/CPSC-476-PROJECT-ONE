import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    GET
#                   URL:    /forums
#                ACTION:    List available discussion forums
#       REQUEST PAYLOAD:    N/A
#   SUCCESSFUL RESPONSE:    HTTP 200 OK
#                           [
#                               {"id": 1, name: "redis", creator: "alice"},
#                               {"id": 2, name: "mongodb", creator: "bob"},
#                           ]
#        ERROR RESPONSE:    NONE: Returns empty array if no forums exist
#      AUTHENTIFICATION:    NO
#                 NOTES:
@app.route('/forums', methods=['GET'])
def printForums():
    # open forums.db table
    # print HTTP 200 OK
    # print all from table
    return "<h1>HTTP 200 OK<h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    POST
#                   URL:    /forums
#                ACTION:    Create a new discussion forum
#       REQUEST PAYLOAD: 
#                           {
#                               "name" : "cassandra"    
#                           }
#   SUCCESSFUL RESPONSE:    HTTP 201 Created
#                           Location header field set to /forums/<forum_id> for new forum
#        ERROR RESPONSE:    HTTP 409 Conflict if forum already exists with same name
#      AUTHENTIFICATION:    YES
#                 NOTES:    Forum's creator is the authenticated user
@app.route('/forums', methods=['POST'])
def addForum():
    # authenticate user and add to variable
    # open forums.db table
    # check if new forum name exists
    # add to table with new forum name and creator
    # set location header field to /forums/<forum_id>
    # if new forum name exists return 409
    try:
        return "<h1>HTTP 201 Created</h1>"
    except:
        return "<h1>HTTP 409 Name Conflict</h1>"
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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
#        ERROR RESPONSE:    HTTP 404 Not Found
#      AUTHENTIFICATION:    NO
#                 NOTES:    The timestamp for a thread is the timestamp to the most recent post to that thread
#                           The creator for a thread is the author of its first post
#                           Threads are listed in reverse chronological order
@app.route('/forums/<forum_id>', methods=['GET'])
def printThreads():
    # Open forum table and search for all threads with correct forum id
    # Print threads in reverse chronological order
    # If forum id does not exist print 404
    try:
        return "<h1>HTTP 200 OK</h1>"
    except:
        return "<h1>HTTP 404 Forum Not Found</h1>"
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
def addThread():
    # Authenticate user and save as variable
    # Open forum table and select all from given forum id
    # Add new thread to forum and set creator to variable
    # Set location header to the new thread
    # If forum id does not exist print 404
    try:
        return "<h1>HTTP 201 Created</h1>"
    except:
        return "<h1>HTTP 404 Forum Not Found</h1>"
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
#      AUTHENTIFICATION:    NO
#                 NOTES:    Posts are listed in chronological order
@app.route('/forums/<forum_id>/<thread_id>', methods=['GET'])
def printComments():
    # Open forum table and select all comments from thread and forum id
    # Print all posts in array in chronological order
    # If forum or thread does not exist print 404
    try:
        return "<h1>HTTP 200 OK</h1>"
    except:
        return "<h1>HTTP 404 Forum/Thread Not Found</h1>"
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
def addComment():
    # Authenticate user
    # Open forum table and select all comments from thread and forum id
    # Get current date and time
    # Add new comment with creator and time
    try:
        return "<h1>HTTP 201 Created</h1>"
    except:
        return "<h1>HTTP 404 Forum/Thread Not Found</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    POST 
#                   URL:    /users 
#                ACTION:    Create a new user 
#       REQUEST PAYLOAD:    
#                           {
#                               "username": "eve",
#                               "password”: "passw0rd"
#                           }
#   SUCCESSFUL RESPONSE:    HTTP 201 Created
#        ERROR RESPONSE:    HTTP 409 Conflict if username already exists
#      AUTHENTIFICATION:    NO
#                 NOTES:    
@app.route('/forums/<forum_id>/<thread_id>', methods=['POST'])
def addUser():
    # Open user's table
    # Check for username if already exists
    # Add username and password
    try:
        return "<h1>HTTP 201 Created</h1>"
    except:
        return "<h1>HTTP 409 Conflict</h1>"

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                METHOD:    PUT 
#                   URL:    /users/<username> 
#                ACTION:    Changes a user’s password 
#       REQUEST PAYLOAD:    
#                           {
#                               "username": "eve",
#                               "password”: "s3cr3t"
#                           }
#   SUCCESSFUL RESPONSE:    HTTP 200 OK
#        ERROR RESPONSE:    HTTP 404 Not found if username does not exist
#                           HTTP 409 Conflict if "username" field does not match the current authenticated user
#      AUTHENTIFICATION:    YES
#                 NOTES:    
@app.route('/users/<username>', methods=['PUT'])
def putUser():
    # Authenticate user
    # If username does not exist return 404
    # If username does not match return 409
    # Overwrite user with new password
    try:
        return "<h1>HTTP 200 OK</h1>"
    except:
        # if username != authUser:
        return "<h1>HTTP 409 Conflict</h1>"
        # elif username == Null:
        return "<h1>HTTP 404 Username Not Found</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

app.run()
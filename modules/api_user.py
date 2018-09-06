import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
def postUser():
    return "<h1>USER</h1>"
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
    return "<h1>PASSWORD</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
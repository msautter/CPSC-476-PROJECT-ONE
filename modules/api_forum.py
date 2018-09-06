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
def getForums():
    return "<h1>FORUMS<h1>"
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
#                           * Location header field set to /forums/<forum_id> for new forum
#        ERROR RESPONSE:    HTTP 409 Conflict if forum already exists with same name
#      AUTHENTIFICATION:    YES
#                 NOTES:    Forum's creator is the authenticated user
@app.route('/forums', methods=['POST'])
def postForum():
    return "<h1>Forum Posted</h1>"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
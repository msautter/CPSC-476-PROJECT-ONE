import sqlite3
dbName = 'database.db'

def checkExists(cur, forum_id, thread_id):
    cur.execute("SELECT * FROM forums WHERE forum_id='{}'".format(str(forum_id)))
    forumsSQL = cur.fetchall()
    if forumsSQL == []:
        return False
    if thread_id != '0':
        cur.execute("SELECT * FROM threads WHERE thread_id='{}'".format(str(thread_id)))
        threadsSQL = cur.fetchall()
        if threadsSQL == []:
            return False
    return True

 

try:
    conn = sqlite3.connect(dbName)
    print("SUCCESS: CONNECTED TO {}".format(str(dbName)))
except:
    print("ERROR: {} OFFLINE".format(str(dbName)))

cur = conn.cursor()

print(str(checkExists(cur, 2, 10)))
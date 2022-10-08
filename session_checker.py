import mysql.connector
from datetime import datetime, timedelta

TOKEN_EXPIRY_TIME = 5 # in hrs 

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database = "databasename"
)
'''
mysql> select * from sessions;
+----+---------+------------------------------------------------+---------------------+---------------------+
| id | user_id | seesion_id                                     | created_at          | updated_at          |
+----+---------+------------------------------------------------+---------------------+---------------------+
|  1 | 1       | 1.23387654324ertyhcjhdhgfycue8t546             | 2022-10-08 15:33:01 | 2022-10-08 15:33:01 |
|  2 | 2       | 1.jtyvcryvhkhg9876545hjhr6rfjgyeteytu76eyrfgre | 2022-10-08 15:33:41 | 2022-10-08 15:33:41 |
+----+---------+------------------------------------------------+---------------------+---------------------+
'''

def verify_user(sessionId, userId):
    try:
    	isValidUser = "Not a valid user"  # default should be False 
    	cur = mydb.cursor()
    	queryString = "SELECT * FROM sessions WHERE user_id={0} LIMIT 1".format(userId)
    	cur.execute(queryString)
    	rowHeaders = [x[0] for x in cur.description]
    	data = cur.fetchall()
    	result = dict(zip(rowHeaders, data[0])) # exception when data = []
    	now = datetime.now()
    	expiry = result['updated_at']

    	if result['seesion_id'] == sessionId:
    		if(now-expiry < timedelta(hours=TOKEN_EXPIRY_TIME)):
    			return "Login successful"
    		else:
    			return "session expired. please login again !!"
    	else:
    		return "user id doesn't match with logged in session"
    	return isValidUser
    except Exception as e:
    	print(e)
    	return "Something went Wrong !"
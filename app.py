from flask import Flask, request
import session_checker
import json
app = Flask(__name__)

import mysql.connector

mydb = mysql.connector.connect( #never hard code credentials  
  host="localhost",
  user="yourusername",
  password="",
  database = "databasename"
)

vulnerable = True # Turn on this flag for testing purpose 

'''
mysql> select * from users;
+----+----------+------------+
| id | username | password   |
+----+----------+------------+
|  1 | kamlesh  | passwor123 |
|  2 | pankaj   | localhost  |
+----+----------+------------+
'''
@app.route('/users/<userId>')
def getUsers(userId):
	returnString= "Oops! this is not your choosen path"

	sessionId = request.cookies.get('sid')
	if not vulnerable:
		res = session_checker.verify_user(sessionId,userId)
		if res != "Login successful":
			return res;

	try:
		cur = mydb.cursor()
		queryString = "SELECT * FROM users WHERE id={0}".format(userId)

		cur.execute(queryString)
		rowHeaders = [x[0] for x in cur.description]
		data = cur.fetchall()

		jsonData = []
		print(data)
		for result in data:
			jsonData.append(dict(zip(rowHeaders, result))) 
		return json.dumps(jsonData)

	except Exception as e:
		return returnString
		

if __name__ == '__main__':
	app.run()
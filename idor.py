import requests 



Host = "127.0.0.1:5000"  #update hostname to qa.mycompany.com or mycompany.com to test IDOR in different environment

endpoints = ["users/1"]

cookies_user1 = {'sid':'1.23387654324ertyhcjhdhgfycue8t546'}
cookies_user2 = {'sid':'1.jtyvcryvhkhg9876545hjhr6rfjgyete'}

headers = {
	"Content-Type": "application/json; charset=utf-8"
}

def login(username , password, user): #user can take 1,2  
	#perform loggin and set cookies 
	return True


def getFullPath(endpoint):
	return "http://"+Host+"/"+endpoint


def checkForIDOR(endpoint):
	try:
		response1 = requests.get(getFullPath(endpoint), headers=headers, cookies=cookies_user1)
		response2 = requests.get(getFullPath(endpoint), headers=headers, cookies=cookies_user2)

		if response1.status_code != 200 or response1.json() is None:
			print("Someting wrong with endpoint: "+ endpoint)
		else:
			if response2.status_code == 200:
				try: 
					response2_str = str(response2.json())
					if response2_str == str(response1.json()):
						print("IDOR found in : "+endpoint)
				except Exception as e: 
					print("NO IDOR : "+endpoint)
	except Exception as e:
		print("Someting went wrong !! ",e)


for endpoint in endpoints:
	checkForIDOR(endpoint)
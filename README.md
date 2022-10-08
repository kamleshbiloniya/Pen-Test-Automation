# Pen-Test-Automation
This repo contains penetration testing automation scripts 

## How to run the app
`export flask_app=app.py`
## Test using following command 
update the cookie value before triggering
`curl -i --cookie "sid=1.23387654324ertyhcjhdhgfycue8t546" 127.0.0.1:5000/users/2` 
## Test IDOR 
` python3 idor.py`

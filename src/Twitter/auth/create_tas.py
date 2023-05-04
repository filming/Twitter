import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1
import requests
import json
from datetime import datetime

load_dotenv()

# create twitter authorized session object
def create_tas():
	
	# getting the env variables and making sure they do exist
	CONSUMER_API_KEY = os.getenv("CONSUMER_API_KEY")
	if CONSUMER_API_KEY == None:
		return 1, ("'CONSUMER_API_KEY' could not be found!",)

	CONSUMER_API_SECRET = os.getenv("CONSUMER_API_SECRET")
	if CONSUMER_API_SECRET == None:
		return 1, ("'CONSUMER_API_SECRET' could not be found!",)

	AUTH_ACCESS_TOKEN = os.getenv("AUTH_ACCESS_TOKEN")
	if AUTH_ACCESS_TOKEN == None:
		return 1, ("'AUTH_ACCESS_TOKEN' could not be found!",)
	
	AUTH_ACCESS_SECRET = os.getenv("AUTH_ACCESS_SECRET")
	if AUTH_ACCESS_SECRET == None:
		return 1, ("'AUTH_ACCESS_SECRET' could not be found!",)

    # using the env variables to create an auth object
	s = requests.Session()
	s.headers.update({"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"})
	s.auth = OAuth1(CONSUMER_API_KEY, CONSUMER_API_SECRET, AUTH_ACCESS_TOKEN, AUTH_ACCESS_SECRET)
	
    # checking to see if the auth object is valid
	r = s.get("https://api.twitter.com/2/users/me", timeout=2)
	resp = json.loads(r.text)
	if r.status_code == 200:
		resp = json.loads(r.text)
		
		current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		logged_in_uid = resp["data"]["id"]
		logged_in_username = resp["data"]["username"]

		print (f"[{current_time}] Started! Logged in as: {logged_in_username}")
		return 0, (s, logged_in_uid, logged_in_username)

	return 1, (r.text,)

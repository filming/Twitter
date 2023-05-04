import json

# this will create a tweet, with possiblities of adding medias and replying to other tweets
def create_tweet(tas, message, media_ids = None, reply_ids = None):
	payload = {"status": message}
	
	if media_ids != None:
		payload["media_ids"] = media_ids
	
	if reply_ids != None:
		payload["in_reply_to_status_id"] = reply_ids
	
	r = tas.post("https://api.twitter.com/1.1/statuses/update.json", data = payload)
	resp = json.loads(r.text)

	if r.status_code == 200:
		tweet_id = resp["id"]
		return 0, tweet_id
	
	return 1, r.text

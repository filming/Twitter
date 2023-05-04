import os
import sys
import json
import time

# takes a list of a media ids and breaks them into groups of 4s if possible
def format_media_ids(media_ids):
	sections = []

	while len(media_ids) > 0:
		part = media_ids[:4]
		sections.append(part)
		media_ids = media_ids[4:]

	for i in range (len(sections)):
		section_string = ",".join(sections[i])
		sections[i] = section_string

	return sections

# takes a file and returns the corresponding media attribute
def get_media_attributes(filepath):
	filepath_parts = filepath.split(".")

	if filepath_parts[len(filepath_parts)-1] == "png":
		return "tweet_image", "image/png"
	
	elif filepath_parts[len(filepath_parts)-1] == "jpeg":
		return "tweet_image", "image/jpeg"
	
	elif filepath_parts[len(filepath_parts)-1] == "gif":
		return "tweet_gif", "image/gif"

	else:
		return "tweet_video", "video/mp4"

def upload_init(tas, media_type, media_category, total_bytes):
	# init
	payload = {
		'command': 'INIT',
		'media_type': media_type,
		'total_bytes': total_bytes,
		'media_category': media_category
	}
	r = tas.post("https://upload.twitter.com/1.1/media/upload.json", data = payload)
	resp = json.loads(r.text)
	media_id = resp['media_id']

	return media_id

def upload_append(tas, filepath, total_bytes, media_id):
	# append
	segment_id = 0
	bytes_sent = 0
	file = open(filepath, 'rb')

	while bytes_sent < total_bytes:
		chunk = file.read(4*1024*1024)
		
		payload = {
			'command': 'APPEND',
			'media_id': media_id,
			'segment_index': segment_id
		}

		files = {
			'media':chunk
		}

		r = tas.post("https://upload.twitter.com/1.1/media/upload.json", data = payload, files = files)
		if r.status_code < 200 or r.status_code > 299:
			print(r.status_code)
			print(r.text)
			sys.exit(0)

		segment_id = segment_id + 1
		bytes_sent = file.tell()

def upload_finalize(tas, media_id):
	# finalize
	payload = {
		'command': 'FINALIZE',
		'media_id': media_id
	}

	r = tas.post("https://upload.twitter.com/1.1/media/upload.json", data = payload)
	resp = json.loads(r.text)

	processing_info = resp.get('processing_info', None)
	
	# status
	while True:
		if processing_info is None:
			return

		state = processing_info['state']

		if state == u'succeeded':
			return

		if state == u'failed':
			sys.exit(0)

		check_after_secs = int(processing_info['check_after_secs'])
		
		time.sleep(check_after_secs)

		payload = {
			'command': 'STATUS',
			'media_id': media_id
		}

		r = tas.get("https://upload.twitter.com/1.1/media/upload.json", params = payload)
		resp = json.loads(r.text)
		
		processing_info = resp.get('processing_info', None)

# takes a file, uploads it to twitter and returns a media id to access the file media
def get_media_id(tas, filepath):
	total_bytes = os.path.getsize(filepath)
	media_category, media_type = get_media_attributes(filepath)

	media_id = upload_init(tas, media_type, media_category, total_bytes)
	upload_append(tas, filepath, total_bytes, media_id)
	upload_finalize(tas, media_id)

	return media_id

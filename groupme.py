import requests

def sendGroupMe(message):

	group_id = '<groud id here>'
	botid = '<your bot id here>'

	botUrl = "https://api.groupme.com/v3/bots/post"

	json = {"text" : message, "bot_id" : botid}

	requests.post(botUrl, json=json)
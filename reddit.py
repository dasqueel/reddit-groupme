import praw
from datetime import datetime, tzinfo, timedelta, time
import pytz
import calendar
import json
from bson import json_util
from groupme import *
from time import sleep

#json file for reddit users last comment datetime
with open('users.json') as df:
    users = json.load(df, object_hook=json_util.object_hook)

#setting time zones correctly with me (eastern) with poloniexs servers
ZERO = timedelta(hours=5)

class UTC(tzinfo):
    def utcoffset(self, dt):
        return ZERO
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return ZERO

utc = UTC()

def to_datetime_from_utc(time_tuple):
    return datetime.fromtimestamp(calendar.timegm(time_tuple), tz=pytz.utc)

#instantiate reddit bot
reddit = praw.Reddit('bot1')

#main function that reads redditors comments and messages you in your choice of messaging app
def reddit():
    redditUsers = []
    for user in redditUsers:
        sleep(2.0)
        #if user hasnt been added to users db, then add him/her
        if user not in users.keys():
            users[user] = datetime.now(utc)

        #date of last redditors comment
        lastDate = users[user]
        #get redditors last 3 commetns
        comments = redditor.comments.new(limit=3)

        #loop through comments to see if any are new
        lastComment = None
        for i, comment in enumerate(comments):
            if i == 0:
                lastComment = datetime.fromtimestamp(comment.created).replace(tzinfo=pytz.UTC) + timedelta(hours=1)
            created = datetime.fromtimestamp(comment.created).replace(tzinfo=pytz.UTC) + timedelta(hours=1)

            #if comment is not older than last posted, break out of loop
            if created < lastDate:
                break
            #send the update to your messanger client, groupme, telegram, sms, etc...
            message = user+' - '+comment.body
            sendGroupMe(message)
            #set the new last posted
            users[user] = lastComment + timedelta(minutes=1)

    #write new users last comment date
    with open('users.json', 'w') as outfile:
            json.dump(users, outfile, default=json_util.default,indent=4, sort_keys=True)

#only run check when you are awake, you can set your own hours
wakeup = time(11)
bed = time(5)
now = datetime.now(utc).time()
def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else:
        return start <= now or now < end


while True:
    #if the time is during the day, run the main function
    if in_between(now,wakeup,bed):
        reddit()
    #dont want to over request reddit servers
    sleep(15.0)

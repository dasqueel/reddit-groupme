import praw
from datetime import datetime, tzinfo, timedelta, time
import pytz
import calendar
import json
from bson import json_util
from groupme import *
from time import sleep

startTime = datetime.now()

#json file for reddit users last comment datetime
with open('users.json') as df:
    users = json.load(df, object_hook=json_util.object_hook)

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

reddit = praw.Reddit('bot1')

def reddit():
        redditUsers = []
        for user in redditUsers:
            sleep(2.0)
            redditor = reddit.redditor(user)
            #if user hasnt been added to users db, then add him/her
            if user not in users.keys():
                users[user] = datetime.now(utc)

            lastDate = users[user]
            comments = redditor.comments.new(limit=3)
            lastComment = None
            for i, comment in enumerate(comments):
                if i == 0:
                    astComment = datetime.fromtimestamp(comment.created).replace(tzinfo=pytz.UTC) + timedelta(hours=1)
                created = datetime.fromtimestamp(comment.created).replace(tzinfo=pytz.UTC) + timedelta(hours=1)
                #print 'created: '+str(created)
                #print 'lastDate: '+str(lastDate)
                if created < lastDate:
                    break
                #send the update to your messanger client, groupme, telegram, sms, etc...
                message = user+' - '+comment.body
                endGroupMe(message)
                #set the new last posted
                users[user] = lastComment + timedelta(minutes=1)

        with open('users.json', 'w') as outfile:
                json.dump(users, outfile, default=json_util.default,indent=4, sort_keys=True)

#only run check when you are awake
wakeup = time(11)
bed = time(5)
now = datetime.now(utc).time()
def in_between(now, start, end):
        if start <= end:
                return start <= now < end
        else: # over midnight e.g., 23:30-04:15
                return start <= now or now < end


while True:
        if in_between(now,wakeup,bed):
                reddit()
        sleep(15.0)

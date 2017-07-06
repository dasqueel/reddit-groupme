# reddit-groupme
recieve groupme messages when a reddit user makes a comment

#### preface:
an rss/push notification like tool.
run reddit.py, and get groupme messages of a redditors comment

you will need some api client secrets and ids first from reddit

info for getting them: https://www.reddit.com/prefs/apps

you also need to create a groupme bot and get your groupme groupid

creating a bot: https://dev.groupme.com/tutorials/bots
finding chats group_id: https://dev.groupme.com/docs/v3

## Installation

clone the repository

```
git clone https://github.com/dasqueel/reddit-groupme.git
```

change into the reddit-groupme directory

```
cd reddit-groupme
```

install requirements

```
pip install -r requirements.txt
```

in groupme.py, set your botid and group_id variables
in praw.ini, set your client_id, client_secret, reddit username and pwd, user_agent variables
in reddit.py, set users you want to follow, ~line 35

```
pip install -r requirements.txt
```

## Usage
```
python reddit.py
```

now wait for the users to make a comment and recieve a groupme message to read it!

test it by adding your reddit username and make a test comment on a thread

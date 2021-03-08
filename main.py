import requests
import os, sys, json
import requests
import tweepy
from tweepy import OAuthHandler

auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_KEY_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])


api = tweepy.API(auth)

ht = api.user_timeline(count=5)

url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
client_id = os.environ["COTOHA_CLIENT_ID"]
client_secret = os.environ["COTOHA_CLIENT_SECRET"]
headers = {
    'Content-Type': 'application/json'
}

data = json.dumps({
    'grantType'   : 'client_credentials',
    'clientId'    : client_id,
    'clientSecret': client_secret
})
res = requests.post(url=url,headers=headers, data=data)
print(res.json())

token = res.json()["access_token"]

def request_cotoha(text, token):
    print(text)
    curl = "https://api.ce-cotoha.com/api/dev/nlp/v1/sentiment"
    cheaders = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': "Bearer " + token
    }
    cdata = json.dumps({
        'sentence' : text # "粉砕、玉砕、大喝采"
    })

    res = requests.post(url=curl, headers=cheaders, data=cdata)
    print(res.json())

for tweet in ht:
    request_cotoha(tweet.text, token)
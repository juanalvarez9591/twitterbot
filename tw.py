import os
import tweepy
import requests

APIKEY = os.environ.get('apikey')
APIKEYSECRET = os.environ.get('apikeysecret')
ACCESSTOKEN = os.environ.get('accesstoken')
ACCESSTOKENSECRET = os.environ.get('accesstokensecret')

INDIRECTAURL = "https://indirectasapi.herokuapp.com/indirecta"

indirecta = requests.get(INDIRECTAURL)

auth = tweepy.OAuthHandler(APIKEY, APIKEYSECRET)
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

if indirecta.status_code == 200:
    api.update_status(indirecta.text)

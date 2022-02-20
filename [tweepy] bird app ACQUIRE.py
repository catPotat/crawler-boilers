#%%
from dotenv import load_dotenv
load_dotenv()
import os
import tweepy

#%%
API_KEY = os.getenv('TWITTER_BOT_KEY')
API_SECRET_KEY = os.getenv('TWITTER_BOT_SECRET_KEY')
BEARER_TOKEN = os.getenv('TWITTER_BOT_BEARER')
callback_uri = 'oob'

#%%
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY, callback_uri)
redirect_url = auth.get_authorization_url()
redirect_url

#%%
PIN = '4921125'
user_pin_input = PIN # input("PIN: ")
access_tok = auth.get_access_token(user_pin_input)
print(access_tok)

# %%

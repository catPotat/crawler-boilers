# %%
import tweepy
from tqdm.auto import tqdm
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('TWITTER_BOT_KEY')
API_SECRET_KEY = os.getenv('TWITTER_BOT_SECRET_KEY')

ACCESS_TOKEN = os.getenv('rbtt_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('rbtt_ACCESS_TOKEN_SECRET')


client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)
client.get_me()


# %%
client.create_tweet(text="tweeted from tweepy v4")

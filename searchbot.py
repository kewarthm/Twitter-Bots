import tweepy
import os
import dotenv

dotenv.load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

api.update_status("Working with tweepy")

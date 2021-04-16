from bot import Bot
from cat_bot import Cat_bot
from bot_v2 import Botv2
import tweepy

class Bot_Factory:

	def __init__(self, consumer_key, consumer_key_secret, access_token, access_token_secret):
		self.consumer_key = consumer_key
		self.consumer_key_secret = consumer_key_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret

	def get_api(self):
		auth = tweepy.OAuthHandler(self.get_consumer_key(), self.get_consumer_key_secret())
		auth.set_access_token(self.get_access_token(), self.get_access_token_secret())
		api = tweepy.API(auth)
		return api

	def get_consumer_key(self):
		return self.consumer_key

	def get_consumer_key_secret(self):
		return self.consumer_key_secret

	def get_access_token(self):
		return self.access_token

	def get_access_token_secret(self):
		return self.access_token_secret
	
	def create_bots(self):
		api = self.get_api()
		return Bot(api), Cat_bot(api), Botv2(api)
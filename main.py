import tweepy
import random
from secret_constants import *
from bot_configs import Bot_configs
from bot import Bot
from cat_bot import Cat_bot
from sys import argv
from random import randint
from time import sleep

MINUMUM_SLEEP_IN_SECONDS = 21600 #6 hours
MAXIMUM_SLEEP_IN_SECONDS = 21600 * 4 #24 hours

def main():
	bot_configs = Bot_configs(consumer_key, consumer_key_secret, access_token, access_token_secret)
	bot, cat_bot = create_bots(bot_configs)
	#bot.retweet_random_tweets_from_list_timeline("")
	#follow_followers_of_account(bot.get_api(), "herbivore_club")

def follow_followers_of_account(api, account_name):
	for i in range(1, 1200):
		followers = api.followers("herbivore_club", cursor=i-2)
		print(followers)
		for j in range(0, len(followers[0])):
			try: 	
				print(followers[0][j].screen_name)
				api.create_friendship(followers[0][j].screen_name)
			except: 
				print("Couldn't follow: " + followers[0][j].screen_name)
				pass
		sleep(5)
		print(i)
	print("done")

def run_on_server():
	print("Starting Bot...")
	bot_configs = Bot_configs(consumer_key, consumer_key_secret, access_token, access_token_secret)
	bot, cat_bot = create_bots(bot_configs)
	bot_functions = get_bot_functions(bot, cat_bot)
	search_terms = get_search_terms()
	print("Successfully created the bots...")

	while (True):
		bot.follow_back_all_followers()
		random.choice(bot_functions)(random.choice(search_terms))
		sleep_until_next_action()
			
def get_bot_functions(bot, cat_bot):
	return [
		bot.steal_popular_tweets_from_search, 
		bot.favourite_random_tweets_from_search, 
		bot.retweet_random_tweets_from_search,
		bot.retweet_random_tweets_from_list_timeline,
		cat_bot.tweet_cat_image
	]
		
def get_search_terms():
	return [
		"#DontTrustRonald",
		"#ImNotLovinIt" 
	]

def sleep_until_next_action():
	sleep_time = randint(MINUMUM_SLEEP_IN_SECONDS,MAXIMUM_SLEEP_IN_SECONDS)
	print("Going to sleep for ", sleep_time, " seconds")
	sleep(sleep_time)

def create_bots(bot_configs):
	api = get_api(bot_configs)
	return Bot(api), Cat_bot(api)

def get_api(bot_configs):
	auth = tweepy.OAuthHandler(bot_configs.get_consumer_key(), bot_configs.get_consumer_key_secret())
	auth.set_access_token(bot_configs.get_access_token(), bot_configs.get_access_token_secret())
	api = tweepy.API(auth)
	return api

def parse_args(args: str) -> bool:
	running_on_server = False
	for arg in args:
		if arg.lower() == 'true':
			running_on_server = True
	return running_on_server

if __name__ == "__main__":
	running_on_server = parse_args(argv[1:])
	if running_on_server:
		run_on_server()
	else:
		main()
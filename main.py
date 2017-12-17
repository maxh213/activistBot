import tweepy
import random
from log_bot import Log_bot
from secret_constants import *
from bot_configs import Bot_configs
from bot import Bot
from cat_bot import Cat_bot
from sys import argv
from random import randint
from time import sleep

MINUMUM_SLEEP_IN_SECONDS = 5
MAXIMUM_SLEEP_IN_SECONDS = 5#21600 #6 hours

def main():
	bot_configs = Bot_configs(consumer_key, consumer_key_secret, access_token, access_token_secret)
	bot, cat_bot, log_bot = create_bots(bot_configs)
	

def run_on_server():
	print("Starting Bot...")
	bot_configs = Bot_configs(consumer_key, consumer_key_secret, access_token, access_token_secret)
	bot, cat_bot, log_bot = create_bots(bot_configs)
	bot_functions = get_bot_functions(bot, cat_bot)
	search_terms = get_search_terms()
	print("Successfully created the bots...")
	log_bot.send_log_dm("Starting!!")

	while (True):
		bot.follow_back_all_followers()
		random.choice(bot_functions)(random.choice(search_terms))
		sleep_until_next_action(log_bot)
			
def get_bot_functions(bot, cat_bot):
	return [
		bot.steal_popular_tweets_from_search, 
		bot.favourite_random_tweets_from_search, 
		bot.retweet_random_tweets_from_search,
		cat_bot.tweet_cat_image
	]
		
def get_search_terms():
	return [
		"#BritanniaCruelty", 
		"#BoycottBritannia",
		"#BoycottNobleFoods",
		"#NotSoNoble"
	]

def sleep_until_next_action(log_bot):
	sleep_time = randint(MINUMUM_SLEEP_IN_SECONDS,MAXIMUM_SLEEP_IN_SECONDS)
	log_text = "Going to sleep for ", sleep_time, " seconds"
	log_bot.send_log_dm(log_text)
	sleep(sleep_time)

def create_bots(bot_configs):
	api = get_api(bot_configs)
	log_bot = Log_bot(api)
	return Bot(api, log_bot), Cat_bot(api, log_bot), log_bot

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
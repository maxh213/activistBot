import tweepy
from secret_constants import *
from bot_configs import Bot_configs
from bot import Bot
from cat_bot import Cat_bot

def main():
	bot_configs = Bot_configs(consumer_key, consumer_key_secret, access_token, access_token_secret)
	bot, cat_bot = create_bots(bot_configs)
	#bot.follow_back_all_followers()
	#bot.retweet_random_tweets_from_home_timeline()
	#bot.favourite_random_tweets_from_home_timeline()
	#bot.steal_popular_tweets_from_search("#notsonoble", 1)
	#cat_bot.tweet_cat_image()

def create_bots(bot_configs):
	api = get_api(bot_configs)
	return Bot(api), Cat_bot(api)

def get_api(bot_configs):
	auth = tweepy.OAuthHandler(bot_configs.get_consumer_key(), bot_configs.get_consumer_key_secret())
	auth.set_access_token(bot_configs.get_access_token(), bot_configs.get_access_token_secret())
	api = tweepy.API(auth)
	return api

if __name__ == "__main__":
    main()
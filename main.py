import tweepy
import random
import os

from waitress import serve
from flask import Flask, render_template, jsonify, request, send_from_directory, send_file, Response

from bot_factory import Bot_Factory
from bot import Bot
from cat_bot import Cat_bot
from bot_v2 import Botv2
from sys import argv
from random import randint
from time import sleep
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_KEY_SECRET = os.getenv('CONSUMER_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
bot_factory = Bot_Factory(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
bot, cat_bot, bot_v2 = bot_factory.create_bots()
def get_bot_functions():
	return [
		#bot.steal_popular_tweets_from_search, 
		bot.favourite_random_tweets_from_search, 
		bot.retweet_random_tweets_from_search,
		cat_bot.tweet_cat_image,
		bot_v2.tweet_trash_at_company,
		bot.follow_followers_of_account
	]
def get_search_terms():
	return [
		"#MorrisonsMisery"
	]
bot_functions = get_bot_functions()
search_terms = get_search_terms()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'})

@app.route('/act', methods=['GET'])
def run():
	#bot.follow_back_followers(5)
	#random.choice(bot_functions)(random.choice(search_terms))
	#bot.favourite_random_tweets_from_search("#MorrisonsMisery")
	bot.follow_followers_of_account("#MorrisonsMisery")
	#bot.retweet_random_tweets_from_search("#MorrisonsMisery")
	#cat_bot.tweet_cat_image("#MorrisonsMisery")
	#bot_v2.tweet_trash_at_company("#MorrisonsMisery")
	return jsonify({'status': 'Complete'})
			
if __name__ == '__main__':
    serve(app, port=8080)
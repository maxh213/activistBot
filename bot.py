import tweepy
from random import *
from status_count import Status_count

class Bot:

	def __init__(self, api):
		self.api = api
		self.CHANCE_OF_RETWEET = 0.05
		self.CHANCE_OF_FAVOURITE = 0.2

	def get_api(self):
		return self.api

	def follow_back_all_followers(self):
		for follower in tweepy.Cursor(self.api.followers).items():
			if not follower.following and not follower.protected:
				follower.follow()
				print ("Just followed: ", follower.screen_name)

	def retweet_random_tweets_from_search(self, query):
		for searchResult in self.api.search(query, tweet_mode="extended"):
			if self.should_do_action_based_on_probablity(self.CHANCE_OF_RETWEET):
				try:
					self.api.retweet(searchResult.id)
					print ("Retweeted: '", searchResult.full_text, "' from the user: ", searchResult.user.screen_name)
				except:
					pass
					#The .retweeted (to check if already retweeded) in search results just flat out don't work so just let it fail

	def favourite_random_tweets_from_search(self, query):
		for searchResult in self.api.search(query, tweet_mode="extended"):
			if self.should_do_action_based_on_probablity(self.CHANCE_OF_FAVOURITE):
				try:
					self.api.create_favorite(searchResult.id)
					print ("Favourited: '", searchResult.full_text, "' from the user: ", searchResult.user.screen_name)
				except:
					pass
					#The .favourited (to check if already favourited) in search results just flat out don't work so just let it fail


	def retweet_random_tweets_from_home_timeline(self):
		statuses = self.api.home_timeline()
		for status in statuses:
			if self.should_do_action_based_on_probablity(self.CHANCE_OF_RETWEET) and not status.retweeted:
				self.api.retweet(status.id)
				print ("Retweeted: '", status.text, "' from the user: ", status.user.screen_name)

	def favourite_random_tweets_from_home_timeline(self):
		statuses = self.api.home_timeline()
		for status in statuses:
			if self.should_do_action_based_on_probablity(self.CHANCE_OF_FAVOURITE) and not status.favorited:
				self.api.create_favorite(status.id)
				print ("Favourited: '", status.text, "' from the user: ", status.user.screen_name)

	def should_do_action_based_on_probablity(self, probability):
		result = uniform(0, 1)
		return result <= probability


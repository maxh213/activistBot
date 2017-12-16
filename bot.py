import tweepy
from random import *
import re

class Bot:

	def __init__(self, api):
		self.api = api

	def get_api(self):
		return self.api

	def follow_back_all_followers(self):
		for follower in tweepy.Cursor(self.api.followers).items():
			if not follower.following:
				follower.follow()
				print ("Just followed: ", follower.screen_name)

	def retweet_random_tweets_from_home_timeline(self):
		chance_of_retweet = 0.05
		statuses = self.api.home_timeline()
		for status in statuses:
			if self.should_do_action_based_on_probablity(chance_of_retweet) and not status.retweeted:
				self.api.retweet(status.id)
				print ("Retweeted: '", status.text, "' from the user: ", status.user.screen_name)

	def favourite_random_tweets_from_home_timeline(self):
		chance_of_favourite = 0.2
		statuses = self.api.home_timeline()
		for status in statuses:
			if self.should_do_action_based_on_probablity(chance_of_favourite) and not status.favorited:
				self.api.create_favorite(status.id)
				print ("Favourited: '", status.text, "' from the user: ", status.user.screen_name)

	def steal_popular_tweets_from_search(self, query, tweet_frequency):
		'''
			TODO:
			-Refactor this
			-check that the same thing isn't tweeted twice
			-create a campaign object
			-create a target object
			-create a trusted retweet/favourite list
			-throw it on the server
			-add generic interests
		'''
		status_counts = []
		for searchResult in self.api.search(query, tweet_mode="extended"):
			text = re.sub(r'http\S+', '', searchResult.full_text)
			added = False
			for status_count in status_counts:
				if status_count[0] == text:
					status_count[1] += 1
					added = True
			if not added:
				status_counts.append([text, 1, searchResult.full_text, searchResult.in_reply_to_status_id])
		for status_count in status_counts:
			if status_count[1] > tweet_frequency:
				try:
					self.api.update_status(status_count[2], in_reply_to_status_id=status_count[3])
					print("Tweeted: '", status_count[2], "'")
					if status_count[3]:
						print("In reply to: '", self.api.get_status(status_count[3].text) ,"'")
				except:
					pass
					#already tweeted it probably
		return self.api.search("#notsonoble")[0]

	def should_do_action_based_on_probablity(self, probability):
		result = uniform(0, 1)
		return result <= probability
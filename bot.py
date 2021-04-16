import tweepy
from tweepy import Cursor
from random import uniform
from time import sleep
from status_count import Status_count

class Bot:

	def __init__(self, api):
		self.api = api
		self.CHANCE_OF_RETWEET = 0.05
		self.CHANCE_OF_FAVOURITE = 0.2
		self.TWEET_FREQUENCY_THRESHOLD = 2

	def get_api(self):
		return self.api

	def follow_back_followers(self, max_amount=3):
		count = 0
		for follower in tweepy.Cursor(self.api.followers).items():
			if not follower.following and not follower.protected:
				follower.follow()
				print ("Just followed: ", follower.screen_name)
				count = count + 1
				if count == max_amount: 
					return
			else:
				print("skipping " + follower + " because they're already followed.")

		
	def follow_followers_of_account(self, _, max_amount=3):
		count = 0
		for follower in Cursor(self.api.followers, screen_name="OpenCagesUK").items():
			if not follower.following and not follower.protected:
				try: 	
					self.api.create_friendship(follower.screen_name)
					print("Followed: " + follower.screen_name)
				except: 
					print("Couldn't follow: " + follower.screen_name)
					pass
				count = count + 1
				if count == max_amount: 
					return
				sleep(1)
			else:
				print("skipping " + follower + " because they're already followed.")

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

	def retweet_random_tweets_from_home_timeline(self, _):
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

	def steal_popular_tweets_from_search(self, query):
		status_counts = self.get_counts_of_popular_tweets(query)
		for status_count in status_counts:
			if status_count.get_count() < self.TWEET_FREQUENCY_THRESHOLD:
				self.steal_tweet(status_count)

	def steal_tweet(self, status_count):
		try:
			self.api.update_status(status_count.get_full_text(), in_reply_to_status_id=status_count.get_in_reply_to_status_id)
			print("Tweeted: '", status_count.get_full_text(), "'")
			if status_count.is_the_status_a_reply:
				print("In reply to: '", self.api.get_status(status_count.get_in_reply_to_status_id().text) ,"'")
		except:
			pass
			#probs already tweeted this tweet
			#it's a pain to check through all your tweets to see if you've tweeted it before btw

	def get_counts_of_popular_tweets(self, query):
		status_counts = []
		for searchResult in self.api.search(query, tweet_mode="extended"):
			new_status_count = Status_count(self.api, searchResult.full_text, self.get_full_text_from_status(searchResult), searchResult.in_reply_to_status_id)
			if not self.does_new_status_count_exist_in_status_counts(new_status_count, status_counts):
				status_counts.append(new_status_count)
		return status_counts

	def get_full_text_from_status(self, status):
		if 'retweeted_status' in dir(status):
			return status.retweeted_status.full_text
		else:
			return status.full_text

	def does_new_status_count_exist_in_status_counts(self, new_status_count, status_counts):
		for status_count in status_counts:
			if status_count.get_match_text() == new_status_count.get_match_text():
				status_count.increment_count()
				return True
		return False
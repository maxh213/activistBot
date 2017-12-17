import tweepy
import re

class Status_count:

	def __init__(self, api, match_text, full_text, in_reply_to_status_id):
		self.api = api
		self.match_text = self.remove_urls_from_match_text(match_text)
		self.full_text = full_text
		self.in_reply_to_status_id = in_reply_to_status_id
		self.count = 1

	def increment_count(self):
		self.count += 1

	def get_count(self):
		return self.count

	def remove_urls_from_match_text(self, match_text):
		return re.sub(r'http\S+', '', match_text)

	def is_the_status_a_reply(self):
		if self.in_reply_to_status_id is None:
			return False
		else: 
			return True

	def get_match_text(self):
		return self.match_text

	def get_full_text(self):
		return self.full_text

	def get_in_reply_to_status_id(self):
		return self.in_reply_to_status_id

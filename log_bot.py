import tweepy

class Log_bot:

	def __init__(self, api):
		self.api = api
		self.LOG_USER_NAME = 'Maxh94'

	def send_log_dm(self, message):
		self.api.send_direct_message(user=self.LOG_USER_NAME, text=message)
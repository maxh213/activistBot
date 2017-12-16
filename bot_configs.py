class Bot_configs:

	def __init__(self, consumer_key, consumer_key_secret, access_token, access_token_secret):
		self.consumer_key = consumer_key
		self.consumer_key_secret = consumer_key_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret

	def get_consumer_key(self):
		return self.consumer_key

	def get_consumer_key_secret(self):
		return self.consumer_key_secret

	def get_access_token(self):
		return self.access_token

	def get_access_token_secret(self):
		return self.access_token_secret
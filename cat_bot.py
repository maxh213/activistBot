import requests
from random import choice
import os

class Cat_bot:

	def __init__(self, api):
		self.api = api
		self.filename = "tmpcat"
		self.directory = "tmp/cats/"
		self.adjectives = [
			"Such a cute kitty!!",
			"mlem",
			"cat go brr",
			"adorable",
			"adorbs",
			"lovable",  
			"charming", 
			"cute", 
			"sweet", 
			"enchanting", 
			"endearing", 
			"dear", 
			"darling", 
			"precious", 
			"delightful", 
			"lovely", 
			"beautiful", 
			"gorgeous", 
			"fetching", 
			"majestic",
			"glorious",
			"distinguished",
			"grand",
			"fluffy",
			"stupidly fluffy",
			"furball"
		]

	def tweet_cat_image(self, _):
		try: 
			url = 'https://api.thecatapi.com/v1/images/search'
			result = requests.get(url)[0]['url']
			filename = 'temp.jpg'
			with open(filename, 'wb') as image:
				for chunk in result:
					image.write(chunk)

			message = self.get_message_of_adoration()
			self.api.update_with_media(filename, status=message)
			os.remove(filename)
			print("Tweeted a cat picture with the message: '", message, "'")
		except:
			print("Failed to tweet a cat picture with the message: '", message, "'")

	def get_message_of_adoration(self):
		return choice(self.adjectives)	
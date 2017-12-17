import cat
import random

class Cat_bot:

	def __init__(self, api):
		self.api = api
		self.filename = "tmpcat"
		self.directory = "tmp/cats/"
		self.adjectives = [
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
		
	def get_png_cat_image(self):
		return cat.getCat(directory=self.directory, filename=self.filename, format='png')

	def get_message_of_adoration(self):
		return random.choice(self.adjectives)

	def tweet_cat_image(self):
		try: 
			cat = self.get_png_cat_image()
			message = self.get_message_of_adoration()
			self.api.update_with_media(filename=cat, status=message)
			print("Tweeted a cat picture with the message: '", message, "'")
		except:
			pass
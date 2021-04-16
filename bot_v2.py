import tweepy
from random import choice

class Botv2:

    def __init__(self, api):
        self.api = api

    def tweet_trash_at_company(self, _):
        try:
            tweet = self.get_tweet_content()
            self.api.update_status(tweet)
            print("Tweeted: '", tweet, "'")
        except:
            pass

    def get_tweet_content(self):
        return choice([
            'Sign up to the better chicken commitment @morrisons! #MorrisonsMisery',
            'Why wont you sign up to the better chicken commitment @morrisons??? #MorrisonsMisery',
            'Customers care about cruelty @morrisons! Sign up to the better chicken commitment and stop selling frankenchickens #MorrisonsMisery',
            'Why do you sell cruelty @Morrisons?? #MorrisonsMisery',
            'Why doesnt @morrisons care about animal cruelty??? #MorrisonsMisery',
            'Sign up to the better chicken commitment and improve the lives of the animals in your supply chain! @Morrisons #MorrisonsMisery',
            'I saw what christ packham said about you on sky news @morrisons! Stop chicken abuse now #MorrisonsMisery',
            'I canny believe this scandle i am seeing from @morrisons??? Such horrible chicken cruelty #MorrisonsMisery',
            'Do us a favour @morrisons and sign up to the better chicken commitment #MorrisonsMisery',
            'Be a good lad @morrisons and sign up to the better chicken commitment, no one want to buy your frankenchicken #MorrisonsMisery',
            'Frankenchicken sold at @morrisons? 🤮🤮🤮 #MorrisonsMisery',
            'Why are you feeding us mutant chicken @morrisons? 🤮 #MorrisonsMisery',
            'Wow! @morrisons really do not care at all what they feed us #frankenchicken #MorrisonsMisery',
            'I did not realise @Morrisons was the worst supermarket for chicken, gross #MorrisonsMisery',
            'Omg @Morrisons why not show some decency and stop selling cruelty #Frankenchicken #MorrisonsMisery',
            'eww just leant about the frankenchicken sold by @Morrisons !!! #MorrisonsMisery',
            'totally will be avoiding @Morrisons in the future #MorrisonsMisery',
            '@Morrisons #MorrisonsMisery',
            '#MorrisonsMisery #MorrisonsMisery #MorrisonsMisery @Morrisons #MorrisonsMisery #MorrisonsMisery #MorrisonsMisery',
            'Jesus, what on earth is all this about @Morrisons selling mutant chicken 🤮 #MorrisonsMisery',
            'Why does @morrisons not care about animals? Those poor chickens must be in so much pain #MorrisonsMisery',
            'Can we all agree to boycott @Morrisons ? So shocked by their cruelty to their animals #MorrisonsMisery',
            'I won''t be shopping at @morrisons anytime soon lol #MorrisonsMisery',
            ' @Morrisons please make a commitment to update your chicken welfare standards, i''m so disappointed! #MorrisonsMisery',
            ' @morrisons 👏Sign👏up👏to👏the👏better👏chicken👏commitment👏#MorrisonsMisery👏',
            'Round of applause to @Morrisons for having such disappointing animal welfare standards 👏👏👏 #MorrisonsMisery',
            'Why haven''t @Morrisons given a reason to why they can''t sign up to the BCC?? #MorrisonsMisery',
            'Please @morrisons, do the right thing and sign up to the better chicken commitment! #MorrisonsMisery',
            'Be a hero for animals @morrisons and sign up to the better chicken commitment #MorrisonsMisery'
        ])
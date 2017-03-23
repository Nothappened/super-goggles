'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'jwkPYpxYjoeqfUYhjo52wjCJV'
MY_CONSUMER_SECRET = 'NWbKiipYhOUJ1q8nJoV7dQSD2eyWNnjLCYE6AWptvUIJDKWyX9'
MY_ACCESS_TOKEN_KEY = '716785803205062658-fspi7ToNDcDWLEWj8WvsVaCKdTwZiRU'
MY_ACCESS_TOKEN_SECRET = 'IO6iYPCuUG4CkTuAxSFH9zYtbq1wPUl3t4S2ZKJ7fl0zQ'

SOURCE_ACCOUNTS = ["BeastsEmbrace"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "AsrielBot" #The name of the account you're tweeting to.


from newscatcherapi import NewsCatcherApiClient
# import time
from dotenv import load_dotenv
import os

load_dotenv(".env")
get_articles_api = NewsCatcherApiClient(x_api_key=os.getenv("api"))

results = get_articles_api.get_latest_headlines(lang='en', countries='in',page_size=10)
# print(results['articles']['title'])
# print(results['articles']['published_date'])
# print(results['articles']['link'])

def getHeadline(message) -> str:
    i_message = message.lower()

    if i_message == 'fetch':
        return (f"{i}. {results['articles'][i]['title']} a quick summary of the headline : {results['articles'][i]['summary']} ")
    
    if i_message == '!help':
        return ("the bot is under development. more functionalities will be added in some time. thank you for showing patience")

    # return ("enter a valid command")
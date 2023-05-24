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


for i in range(1,10):
    print(f"{i}. {results['articles'][i]['title']} a quick summary of the headline : {results['articles'][i]['summary']} ")
    
# print("the bot is under development. more functionalities will be added in some time. thank you for showing patience")

    # return ("enter a valid command")
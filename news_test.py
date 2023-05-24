from newscatcherapi import NewsCatcherApiClient
# import time
from dotenv import load_dotenv
import os

load_dotenv(".env")
get_articles_api = NewsCatcherApiClient(x_api_key=os.getenv("api"))

results = get_articles_api.get_latest_headlines(lang='en', countries='us',page_size=10)
# print(results['articles']['title'])
# print(results['articles']['published_date'])
# print(results['articles']['link'])


for i in range(1,2):
    print(f"{i}. News section : {results['articles'][i]['topic']} {results['articles'][i]['title']} a quick summary of the headline : {results['articles'][i]['summary']}. news is from {results['articles'][i]['country']} ")

# k = results['articles'][0]
# print(k.keys())

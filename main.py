from newscatcherapi import NewsCatcherApiClient
import time
from dotenv import load_dotenv
import os

# api = '_kieLqn_kqG_KdbmyXMz83r0HrB_eUejOcwWfz870SE'
load_dotenv(".env")
get_articles_api = NewsCatcherApiClient(x_api_key=os.getenv("api"))

results = get_articles_api.get_latest_headlines(lang='en', countries='in',page_size=10)
# print(results['articles']['title'])
# print(results['articles']['published_date'])
# print(results['articles']['link'])

for i in range(1,10):
    print(f"{i}. {results['articles'][i]['title']} a quick summary of the headline : {results['articles'][i]['summary']} ")
    time.sleep(4)
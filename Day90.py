# Exercise 10: News App in Python

# use the newsapi and the requests module to fetch the daily news related to different topics.

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json

load_dotenv()

apiKey = os.getenv('API_KEY')

def get_news(topic):
    URL = f'https://newsapi.org/v2/everything?q={topic}&from=2026-02-18&to=2026-02-18&sortBy=popularity&apiKey={apiKey}'
    
    response = requests.get(URL)
    news = json.loads(response.text)

    for article in news.get('articles'):
        print(article['title'])
        print(article['description'])
        print('-------------------------------------------------------')

topic = input('Enter topic to get news on: ')
get_news(topic)

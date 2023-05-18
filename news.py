from newsapi import NewsApiClient
import random
from termcolor import colored
newsapi = NewsApiClient(api_key='247ece99b66d48929b6aa3b541ac168f')

def get_news(category):
    """This method generates news using 'news Api'."""
    top_headlines = newsapi.get_top_headlines(
        country='in',
        category=category
    )
    articles = top_headlines.get('articles', [])
    article = random.choice(articles)
    Title = article['title']
    Description = article['description']
    Url = article['url']
    text = f"\n\n{Title}\n\n{Description}\n\n{Url}"
    return text
#print(get_news("sports"))


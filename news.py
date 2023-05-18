from newsapi import NewsApiClient
import random
from termcolor import colored
newsapi = NewsApiClient(api_key='YOUR_API_KEY')

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


import random
from newsapi import NewsApiClient
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
    text = f"Title: {Title}\n\n{Description}"
    return text
# print(get_news("sports"))

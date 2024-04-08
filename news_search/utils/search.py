from datetime import datetime, timedelta
from newsapi import NewsApiClient


def search_news(topic: str, api_key: str, lang: str = "en", max_news: int = 15):
    # Your function implementation

    # Initialize News API client
    newsapi = NewsApiClient(api_key=api_key)


    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    # Fetch news articles
    articles = newsapi.get_everything(q=topic,
                                      from_param=start_date.strftime('%Y-%m-%d'),
                                      to=end_date.strftime('%Y-%m-%d'),
                                      language=lang,
                                      sort_by='relevancy')

    # Extract relevant information from articles
    result = []
    for article in articles['articles'][:max_news]:
        result.append({
            'title': article['title'],
            'url': article['url'],
            'published_at': article['publishedAt']
        })

    return result, articles
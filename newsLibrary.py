from newsapi import NewsApiClient

# Initialize News API Client
newsapi = NewsApiClient(api_key='815ccaed069649b193f7d196557b5e55')

def get_news():
    """Fetch top news headlines using NewsAPI"""
    top_headlines = newsapi.get_top_headlines(language='en', country='in')
    
    articles = top_headlines.get('articles')
    if not articles:
        return "Sorry, I couldn't fetch any news at the moment."

    # Fetch top 5 headlines
    headlines = [article['title'] for article in articles[:5]]
    return headlines

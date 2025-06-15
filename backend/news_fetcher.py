# backend/news_fetcher.py

import requests
from backend.config import NEWS_API_KEY, CATEGORIES, DEFAULT_COUNTRY

BASE_URL = "https://newsapi.org/v2"

def get_news_by_category(category):
    """Fetch news by category (e.g., 'politics', 'sports')"""
    if category not in CATEGORIES:
        return []  # Invalid category
    
    url = f"{BASE_URL}/top-headlines"
    params = {
        "category": CATEGORIES[category],  # Translate to NewsAPI's category
        "country": DEFAULT_COUNTRY,
        "apiKey": NEWS_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error if API call fails
        return response.json().get("articles", [])
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def search_news(query):
    """Search news by keyword (e.g., 'NASA', 'AI')"""
    url = f"{BASE_URL}/everything"
    params = {
        "q": query,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("articles", [])
    except Exception as e:
        print(f"Error searching news: {e}")
        return []
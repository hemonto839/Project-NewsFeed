# backend/config.py

NEWS_API_KEY = "e5c73a66b5f544cb802a573611405645"  # Replace with your NewsAPI key

# Map your app's categories to NewsAPI's categories
CATEGORIES = {
    "politics": "politics",
    "sports": "sports",
    "science": "science",
    "technology": "technology",
    "defense": "general",  # NewsAPI doesn't have "defense", so we use "general"
    "study": "general"     # Same for "study"
}

DEFAULT_COUNTRY = "us"  # Default country for news
# backend/main.py

from flask import Flask, jsonify, request
from backend.news_fetcher import get_news_by_category, search_news
from backend.config import CATEGORIES

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to NewsFeed App! Use /category/<name> or /search?q=query"

# Route to fetch news by category
@app.route("/category/<category>")
def news_category(category):
    if category not in CATEGORIES:
        return jsonify({"error": "Invalid category"}), 400
    
    articles = get_news_by_category(category)
    return jsonify({"category": category, "articles": articles})

# Route to search news
@app.route("/search")
def news_search():
    query = request.args.get("q", "")  # Get search query from URL (?q=...)
    if not query:
        return jsonify({"error": "Missing search query"}), 400
    
    articles = search_news(query)
    return jsonify({"query": query, "articles": articles})

if __name__ == "__main__":
    app.run(debug=True)  # Run the server
from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    api_key = os.getenv('NEWSDATA_API_KEY')
    
    if not api_key:
        logger.error("API key not found in environment variables")
        return jsonify({'error': 'API key not found, see README.md'}), 500
    
    # Log API key status (without exposing the key)
    logger.debug(f"API key present: {'Yes' if api_key else 'No'}")
    logger.debug(f"API key length: {len(api_key) if api_key else 0}")
    
    url = f'https://newsdata.io/api/1/news?apikey={api_key}&q={query}'
    logger.debug(f"Making request to NewsData.io API with query: {query}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        logger.debug(f"API Response status: {data.get('status', 'unknown')}")
        
        if 'status' in data and data['status'] == 'error':
            error_msg = data.get('message', 'Unknown error')
            logger.error(f"API Error: {error_msg}")
            return jsonify({'error': error_msg}), 500
            
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        if '401' in str(e):
            return jsonify({'error': 'Invalid API key. Please check your NewsData.io API key in the .env file.'}), 401
        return jsonify({'error': f'Failed to fetch news: {str(e)}'}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

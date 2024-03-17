from flask import Flask, jsonify, request
import json
import logging
from controllers import fetch_documents, get_sitemap
import os

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Initialize Flask app
app = Flask(__name__)

# Setup logging
logging.basicConfig(level=config['logging']['level'], format=config['logging']['format'])
logger = logging.getLogger(config['service_name'])

@app.route(config['api_interaction']['fetch_document']['endpoint'], methods=['GET'])
def fetch_docs():
    """
    Endpoint to fetch documents from the specified URLs.
    """
    url = request.args.get('url')  # Get URL from query parameters
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    try:
        docs = fetch_documents(url)
        return jsonify(docs), 200
    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        return jsonify({"error": "Failed to fetch documents"}), 500

@app.route(config['api_interaction']['get_sitemap']['endpoint'], methods=['GET'])
def api_get_sitemap():
    """
    Endpoint to get the sitemap of the documentation URLs.
    """
    base_url = request.args.get('url')  # Get base URL from query parameters
    if not base_url:
        return jsonify({"error": "URL parameter is required"}), 400
    sitemap = get_sitemap(base_url)
    return jsonify(sitemap)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))  # Adjust host and port as needed

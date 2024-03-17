# views.py
# This file is intended to define the view functions for the Flask application.
# However, in the provided project structure, the view functions are already defined within app.py.
# Typically, in a Flask project, views.py would contain route definitions and their corresponding view functions.
# Given the existing project setup, it seems there's a misunderstanding in the project structure.
# For clarity and following Flask's convention, view functions are usually defined in views.py or directly within app.py.
# Since the view functions are already implemented in app.py, this file would not be necessary unless we refactor the code to move the view functions here and import them into app.py.

# A refactored approach could look like this:

from flask import jsonify
from controllers import fetch_docs_controller, get_sitemap_controller
import logging

# Assuming logger is configured in app.py or another module
logger = logging.getLogger("LangchainDocsFetcher")

def fetch_docs():
    """
    Endpoint to fetch documents from the specified URLs.
    """
    try:
        docs = fetch_docs_controller.fetch_documents()
        return jsonify(docs), 200
    except Exception as e:
        logger.error(f"Error fetching documents: {e}")
        return jsonify({"error": "Failed to fetch documents"}), 500

def get_sitemap():
    """
    Endpoint to get the sitemap of the documentation URLs.
    """
    try:
        sitemap = get_sitemap_controller.get_sitemap()
        return jsonify(sitemap), 200
    except Exception as e:
        logger.error(f"Error getting sitemap: {e}")
        return jsonify({"error": "Failed to get sitemap"}), 500

# Note: If you decide to refactor and use this views.py, you need to import these functions in app.py and set up the routes there.
# Example in app.py after refactoring:
# from views import fetch_docs, get_sitemap
# app.route(config['api']['endpoints']['fetch_docs'], methods=['GET'])(fetch_docs)
# app.route(config['api']['endpoints']['get_sitemap'], methods=['GET'])(get_sitemap)


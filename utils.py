
import requests
from bs4 import BeautifulSoup
import logging
import json

def load_config():
    """
    Loads the configuration from the config.json file.
    """
    with open('config.json') as config_file:
        return json.load(config_file)

def fetch_url_content(url):
    """
    Fetches the content of a given URL using requests and returns the raw HTML.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch URL {url}: {e}")
        return None

def parse_html_for_sitemap(html_content):
    """
    Parses the given HTML content using BeautifulSoup to extract all links and return them as a list.
    This can be used to generate a simple sitemap.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    sitemap = []
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            sitemap.append(href)
    return sitemap

def parse_html_for_docs(html_content):
    """
    Parses the given HTML content using BeautifulSoup to extract document-like content.
    This example extracts paragraphs, but it can be adjusted based on the actual structure of the target documentation.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    docs = [paragraph.text for paragraph in paragraphs]
    return docs

def log_error(message):
    """
    Logs an error message to the console. This is a simple wrapper around logging.error for potential future enhancements.
    """
    logging.error(message)

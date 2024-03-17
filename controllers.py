# controllers.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def fetch_documents(url):  # Add URL parameter
    """
    Controller to fetch documents from the specified URLs.
    This function will be called by the fetch_docs view function.
    """
    # Example URL to start with, this should be dynamic or configured
    urls = [url]  # Use the provided URL
    documents = []

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Assuming we want to fetch all paragraph texts as documents
                paragraphs = soup.find_all('p')
                for paragraph in paragraphs:
                    documents.append(paragraph.text)
        except Exception as e:
            # Log error or handle it as needed
            print(f"Error fetching documents from {url}: {e}")

    return documents

def get_sitemap(base_url):  # Add base_url parameter
    # Use the provided base_url instead of a hardcoded one
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = set()  # Use a set to avoid duplicates
            for link in soup.find_all('a', href=True):
                href = link['href']
                # Create an absolute URL
                absolute_url = urljoin(base_url, href)
                # Filter for URLs containing '/docs'
                if '/docs' in absolute_url:
                    links.add(absolute_url)
            return {"urls": list(links)}
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return {"error": "Failed to fetch sitemap"}

def fetch_internal_links(url):
    """
    Fetches all internal links from a given documentation URL.
    """
    try:
        response = requests.get(url)
        domain = urlparse(url).netloc
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            internal_links = set()
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('/') or urlparse(href).netloc == domain:
                    internal_links.add(urljoin(url, href))
            return list(internal_links)
    except Exception as e:
        print(f"Error fetching internal links from {url}: {e}")
        return []

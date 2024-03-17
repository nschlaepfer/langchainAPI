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

def fetch_all_links_from_docs(base_url):
    """
    Fetches all links from the documentation route of a given website.
    """
    try:
        # Ensure base_url ends with '/docs'
        if not base_url.endswith('/docs'):
            base_url = urljoin(base_url, '/docs')

        visited = set()  # Keep track of visited URLs to avoid infinite loops
        to_visit = {base_url}  # Start with the base URL
        all_links = set()  # Store all unique links found

        while to_visit:
            current_url = to_visit.pop()
            if current_url in visited:
                continue
            visited.add(current_url)

            response = requests.get(current_url)
            if response.status_code != 200:
                continue  # Skip URLs that are not successfully fetched

            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(current_url, href)
                if absolute_url.startswith(base_url) and absolute_url not in visited:
                    to_visit.add(absolute_url)  # Add internal links to to_visit
                all_links.add(absolute_url)  # Add all links to all_links

        return list(all_links)
    except Exception as e:
        print(f"Error fetching all links from {base_url}: {e}")
        return []

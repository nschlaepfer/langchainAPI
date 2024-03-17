
import unittest
from unittest.mock import patch
from controllers import fetch_documents, get_sitemap
from utils import fetch_url_content, parse_html_for_docs

class TestFetchDocs(unittest.TestCase):

    @patch('controllers.requests.get')
    def test_fetch_documents_success(self, mock_get):
        # Mocking the requests.get response
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b"<html><body><p>Document 1 content</p><p>Document 2 content</p></body></html>"

        documents = fetch_documents()
        self.assertEqual(len(documents), 2)
        self.assertIn("Document 1 content", documents)
        self.assertIn("Document 2 content", documents)

    @patch('controllers.requests.get')
    def test_fetch_documents_failure(self, mock_get):
        # Mocking the requests.get to simulate a failure
        mock_get.return_value.status_code = 404

        documents = fetch_documents()
        self.assertEqual(len(documents), 0)

    @patch('utils.requests.get')
    def test_fetch_url_content(self, mock_get):
        # Mocking the requests.get response for fetch_url_content
        expected_html = "<html></html>"
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = expected_html

        url = "https://python.langchain.com/docs/get_started/introduction"
        content = fetch_url_content(url)
        self.assertEqual(content, expected_html)

    def test_parse_html_for_docs(self):
        html_content = "<html><body><p>Test Paragraph 1</p><p>Test Paragraph 2</p></body></html>"
        docs = parse_html_for_docs(html_content)
        self.assertEqual(len(docs), 2)
        self.assertIn("Test Paragraph 1", docs)
        self.assertIn("Test Paragraph 2", docs)

    def test_get_sitemap(self):
        sitemap = get_sitemap()
        self.assertTrue(isinstance(sitemap, dict))
        self.assertIn("urls", sitemap)
        self.assertTrue(isinstance(sitemap["urls"], list))
        self.assertIn("https://python.langchain.com/docs/get_started/introduction", sitemap["urls"])

if __name__ == '__main__':
    unittest.main()


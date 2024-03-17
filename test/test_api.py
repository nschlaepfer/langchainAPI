
import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fetch_docs(self):
        response = self.app.get('/fetch_docs')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(data, list)
        # Assuming the fetch_documents function returns a list of paragraphs
        # from the "https://python.langchain.com/docs/get_started/introduction" page
        self.assertTrue(len(data) > 0)
        self.assertIsInstance(data[0], str)

    def test_get_sitemap(self):
        response = self.app.get('/get_sitemap')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(data, dict)
        self.assertIn('urls', data)
        self.assertIsInstance(data['urls'], list)
        # Assuming the get_sitemap function returns a static list of URLs
        # including "https://python.langchain.com/docs/get_started/introduction"
        self.assertTrue("https://python.langchain.com/docs/get_started/introduction" in data['urls'])

if __name__ == '__main__':
    unittest.main()


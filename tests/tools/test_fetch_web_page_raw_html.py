import unittest
from tools import fetch_web_page_raw_html

class TestFetchWebPageRawHtml(unittest.TestCase):
    def test_fetch_full_page(self):
        url = "https://example.com"
        result = fetch_web_page_raw_html.fetch_web_page_raw_html.invoke({ "url": url })
        self.assertIn("<body>", result)
        self.assertIn("</body>", result)

if __name__ == '__main__':
    unittest.main()

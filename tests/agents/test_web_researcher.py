import unittest

from agents.web_researcher import web_researcher

class TestWebResearcher(unittest.TestCase):
    def test_web_researcher(self):
        self.assertTrue(callable(web_researcher))

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch

from tools import request_human_input

class TestRequestHumanInput(unittest.TestCase):
    @patch('builtins.input', return_value='test input')
    def test_request_human_input(self, mock_input):
        result = request_human_input.request_human_input.invoke({ "prompt": "Enter something: " })
        self.assertEqual(result, 'test input')

if __name__ == '__main__':
    unittest.main()

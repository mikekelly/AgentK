import unittest
import os
from tools import read_file

class TestReadFile(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file_path = 'test_file.txt'
        with open(self.test_file_path, 'w') as file:
            file.write('Hello, world!')

    def tearDown(self):
        # Remove the temporary file after test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_file(self):
        content = read_file.read_file.invoke({ 'file_path': self.test_file_path })
        self.assertEqual(content, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()

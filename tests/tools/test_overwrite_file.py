import unittest
import os

from tools import overwrite_file

class TestOverwriteFile(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file_path = 'test_file.txt'
        with open(self.test_file_path, 'w') as f:
            f.write('Initial content')

    def tearDown(self):
        # Remove the temporary file after test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_overwrite_file(self):
        # Overwrite the file with new content
        result = overwrite_file.overwrite_file.invoke({ 'file_path': self.test_file_path, 'content': 'New content' })
        
        # Check the result message
        self.assertEqual(result, f'File at {self.test_file_path} has been successfully overwritten.')
        
        # Verify the file content
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'New content')

if __name__ == '__main__':
    unittest.main()
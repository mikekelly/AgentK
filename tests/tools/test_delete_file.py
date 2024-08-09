import unittest
import os
from tools import delete_file

class TestDeleteFile(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.test_file_path = 'test_file.txt'
        with open(self.test_file_path, 'w') as f:
            f.write('This is a test file.')

    def test_delete_file(self):
        # Test deleting the file
        result = delete_file.delete_file.invoke({ 'file_path': self.test_file_path })
        self.assertEqual(result, f'File at {self.test_file_path} has been deleted successfully.')
        self.assertFalse(os.path.exists(self.test_file_path))

    def tearDown(self):
        # Clean up any remaining test files
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

if __name__ == '__main__':
    unittest.main()

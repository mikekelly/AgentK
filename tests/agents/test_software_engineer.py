import unittest

from agents.software_engineer import software_engineer

class TestSoftwareEngineer(unittest.TestCase):
    def test_software_engineer(self):
        self.assertTrue(callable(software_engineer))

if __name__ == '__main__':
    unittest.main()

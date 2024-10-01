#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a new FileStorage instance for testing."""
        self.storage = FileStorage()

    def test_file_path(self):
        """Test that the file_path is correctly initialized."""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

if __name__ == '__main__':
    unittest.main()

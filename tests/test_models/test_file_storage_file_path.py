#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorageFilePath(unittest.TestCase):
    """Test class for FileStorage's __file_path attribute."""

    def setUp(self):
        """Set up a FileStorage instance for testing."""
        self.storage = FileStorage()

    def test_file_path_exists(self):
        """Test if __file_path is correctly initialized."""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'), "File path is not set.")
        self.assertEqual(self.storage._FileStorage__file_path, "file.json", "Incorrect file path.")
    
    def test_file_path_is_string(self):
        """Test if __file_path is a string."""
        self.assertIsInstance(self.storage._FileStorage__file_path, str, "__file_path is not a string.")

if __name__ == "__main__":
    unittest.main()

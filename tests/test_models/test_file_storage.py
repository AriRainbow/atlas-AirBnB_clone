#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up a fresh environment for each test."""
        self.storage = FileStorage()  # Create a new storage instance
        self.storage.reload()  # Load any existing dats to start fresh
        self.test_file = self.storage._FileStorage__file_path  # Access the private attribute for cleanup

    def tearDown(self):
        """Cleanup after each test."""
        try:
            os.remove(self.test_file)  # Remove the test JSON file if it exists
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error removing file: {e}")

    def test_save(self):
        """Test if the save method works as expected."""
        obj1 = BaseModel()  # Create a new BaseModel instance
        self.storage.new(obj1)  # Add the object to storage
        self.storage.save()  # Save to file

        # Reload storage to check if the object is saved correctly
        self.storage.reload()  # Reload to ensure the saved data is loaded
        obj_key = f"BaseModel.{obj1.id}"  # Construct the key for the stored object

        # Check if the object is in storage
        self.assertIn(obj_key, self.storage.all(), "Object not found after saving.")

        # Assert that the saved object matches the original
        saved_obj = self.storage.all()[obj_key]
        self.assertEqual(saved_obj.to_dict(), obj1.to_dict(), "Saved object does not match original.")

    def test_file_path(self):
        """Test that the file_path is correctly initialized."""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

if __name__ == '__main__':
    unittest.main()

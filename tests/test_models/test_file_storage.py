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

        # Check if file exists
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path), "File not found after save.")
        
        self.storage.reload()  # Reload to ensure the saved data is loaded
        obj_key = f"BaseModel.{obj1.id}"  # Construct the key for the stored object

        # Check if the object is in storage
        self.assertIn(obj_key, self.storage.all(), "Object not found after saving.")

        # Assert that the saved object matches the original
        saved_obj = self.storage.all()[obj_key]
        self.assertEqual(saved_obj.to_dict(), obj1.to_dict(), "Saved object does not match original.")

        # Check the count of objects after saving
        self.assertEqual(self.storage.count_objects(), 1, "Object count after saving is incorrect.")

    def test_file_path(self):
        """Test that the file_path is correctly initialized."""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_object_creation(self):
        """Test object creation and count."""
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.assertEqual(self.storage.count_objects(), 1)  # Ensure one object is stored

    def test_count_objects(self):
        """Test if count_objects returns the correct number of stored objects."""
        initial_count = self.storage.count_objects()
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()
        self.assertEqual(self.storage.count_objects(), initial_count + 1, "Count of objects is incorrect after saving.")

    def test_reload(self):
        """Test if reload correctly loads objects from file."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        
        # Add objects to storage
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()  # Save to file

        # Clear objects from storage
        self.storage.all().clear()  # This should be the equivalent of deleting all objects

        # Now reload from file
        self.storage.reload()

        # Ensure that the objects are back in storage after reload
        obj1_key = f"BaseModel.{obj1.id}"
        obj2_key = f"BaseModel.{obj2.id}"

        self.assertIn(obj1_key, self.storage.all(), "Object 1 not found after reload.")
        self.assertIn(obj2_key, self.storage.all(), "Object 2 not found after reload.")

        # Assert that the loaded object matches the original
        self.assertEqual(self.storage.all()[obj1_key].to_dict(), obj1.to_dict(), "Loaded object 1 does not match original.")
        self.assertEqual(self.storage.all()[obj2_key].to_dict(), obj2.to_dict(), "Loaded object 2 does not match original.")

if __name__ == '__main__':
    unittest.main()

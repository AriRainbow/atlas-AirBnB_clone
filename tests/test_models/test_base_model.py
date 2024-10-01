#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_instance_creation(self):
        """Test if a new instance is correctly created."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.create_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        """Test if save method updates updated_at."""
        model = BaseModel
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test if to_dict returns correct dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_init_with_kwargs(self):
        """Test creating ann instance from a dictionary (kwargs)."""
        # Create an initial instance
        base = BaseModel()
        base.name = "My First Model"
        base.my_number = 89
        base_dict = base.to_dict()

        # Create a new instance using dictionary (kwargs)
        new_base = BaseModel(**base_dict)

        # Check if the IDs are the same
        self.assertEqual(base.id, new_base.id)

        # Check if the create_at and updated_at are converted back to datetime
        self.assertEqual(base.created_at, new_base.created_at)
        self.assertEqual(base.my_number, new_base.my_number)

    def test_init_no_kwargs(self):
        """Test creating an instance without kwargs (normal initialization)."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)

    def test_base_model_created_from_dict(self):
        """Test BaseModel creation from a dictionary."""
        model_dict = {
            'id': '12345',
            'created_at': '2024-10-01T04:33:36.270837',
            'updated_at': '2024-10-01T04:33:36.270843'
        }
        
        model_instance = BaseModel(**model_dict)
        
        self.assertEqual(model_instance.id, '12345')
        self.assertEqual(model_instance.created_at, datetime.strptime('2024-10-01T04:33:36.270837', "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_instance.updated_at, datetime.strptime('2024-10-01T04:33:36.270843', "%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == "__main__":
    unittest.main()
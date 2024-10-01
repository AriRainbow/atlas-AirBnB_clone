#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    # Correct format: use 'T%H:%M:%S' instead of '%T%H:%S'
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the updated_at attributes to the current time."""
        self.updated_at = datetime.now()
        from models import storage  # Dynamic import to avoid cicular import
        print(f"Saving {self.__class__.__name__} instance with ID: {self.id}")
        storage.save()  # Save the storage to file

    def to_dict(self):
        """Return a dictionary representaion of the instance,"""
        dict_rep = self.__dict__.copy()  # Copy current attributes
        dict_rep['__class__'] = self.__class__.__name__  # Add class name to the dictionary
        dict_rep['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO string
        dict_rep['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO string
        return dict_rep

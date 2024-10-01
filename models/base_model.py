#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model."""
        if kwargs:
            for key, value in kwargs.itmes():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%d%T%H:%S.%f"))
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

    def to_dict(self):
        """Return a dictionary representaion of the instance,"""
        dict_rep = self.__dict__.copy()  # Copy current attributes
        dict_rep['__class__'] = self.__class__.__name__  # Add class name to the dictionary
        dict_rep['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO string
        dict_rep['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO string
        return dict_rep

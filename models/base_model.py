#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in AirBnB clone project."""

    def __init__(self):
        """Initializes a new BaseModel instance."""
        self.id = str(uuid.uuid4())  # Assign a unique id
        self.created_at = datetime.now()  # Set the creation time
        self.updated_at = self.created_at  # Set the updated time to match creation initially

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

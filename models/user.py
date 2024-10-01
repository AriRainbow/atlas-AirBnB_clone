#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize the User instance."""
        super().__init__(*args, **kwargs)  # Call BaseModel's initializer
        # You can add any specific attributes for User here
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

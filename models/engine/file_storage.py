#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class to serialize and deserialize instances to/from a JSON file."""

    def __init__(self):
        self.__file_path = "file.json"  # path to the JSON file
        self.__objects = {}  # stores all objects

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"  # Fixed key formatting
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
                for key, value in self.__objects.items():
                    # Create an instance of the class from the dictionary
                    class_name = value.pop("__class__")  # Remove __class__ key
                    # Import classes here to avoid circular import
                    from models.base_model import BaseModel
                    from models.user import User
                    
                    classes = {
                        "BaseModel": BaseModel,
                        "User": User
                        # Add other class mappings as needed
                    }
                    if class_name in classes:
                        self.__objects[key] = classes[class_name](**value)
                    else:
                        print(f"Warning: Class '{class_name}' not found.")

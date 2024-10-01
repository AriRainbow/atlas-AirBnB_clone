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
        print("Saving the following objects to JSON:")
        for key, obj in self.__obkects.itmes():
            print(f"Object {key}: {obj}")

        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                loaded_data = json.load(f)  # Load JSON data
                print("Loaded data from JSON:")
                print(loaded_data)
                for key, value in loaded_data.items():
                    class_name = value.pop("__class__", None)  # Remove __class__ key

                    # Ensure the class name exists in the saved data
                    if not class_name:
                        print(f"Warning: No class name found for object {key}")
                        continue

                    # Import classes here to avoid circular import
                    from models.base_model import BaseModel
                    from models.user import User
                    
                    # Map class names to actual classes
                    classes = {
                        "BaseModel": BaseModel,
                        "User": User
                        # Add other class mappings as needed
                    }

                    # Check if class_name exists in classes
                    if class_name in classes:
                        print(f"Restoring objects {key} of class {class_name}")
                        # Dynamically create an instance from the class using the dictionary value
                        self.__objects[key] = classes[class_name](**value)
                    else:
                        print(f"Warning: Class '{class_name}' not found.")

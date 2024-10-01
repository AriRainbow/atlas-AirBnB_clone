#!/usr/bin/python3
import json
import os


class FileStorage:
    """Class to serialize and deserialize instances to/from a JSON file."""

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # stores all objects

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj,__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.objects = json.load(f)
                for key, value in self.__objects.items():
                    # Create an instance of the class from the dictionary
                    class_name = value["__class__"]
                    self.__objects[key] = eval(class_name)(**value)

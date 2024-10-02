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

    # @property
    # def objects(self):
        # """Expose __objects as a property."""
        # return self.__objects

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"  # Fixed key formatting
        self.__objects[key] = obj  # Ensure the object is properly stored

    def save(self):
        """Serializes __objects to the JSON file."""
        try:
            with open(self.__file_path, 'w') as f:
                # Create a dictionary representation of all objects
                data = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
                # Serialize the data to JSON and write it to the file
                json.dump(data, f)
            return True  # Ensures that it returns True after saving
        except (IOError, json.JSONDecodeError):
            return False  # Return False if there was an error
        except Exception as e:
            return False  # Handle any other exception

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                loaded_data = json.load(f)  # Load JSON data
                for key, value in loaded_data.items():
                    class_name = value.pop("__class__", None)
                    # Remove __class__ key

                    if not class_name:
                        continue

                    # Import classes here to avoid circular import
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.place import Place
                    from models.state import State
                    from models.city import City
                    from models.review import Review
                    from models.amenity import Amenity

                # Map class names to actual classes
                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Place": Place,
                    "State": State,
                    "City": City,
                    "Review": Review,
                    "Amenity": Amenity
                }

                # Ensure class name is retrieved correctly from the dictionary
                if class_name in classes:
                    cls = classes.get(class_name)
                    # Retrieve the class object from the classes dictionary
                    self.objects[key] = cls(**value)
                    # Instantiate the class using the saved dictionary

    def get_objects(self):
        """Returns the objects stored in __objects."""
        return self.__objects  # Accessing __objects directly is fine here

    def count_objects(self):
        """Returns the number of objects stored."""
        return len(self.__objects)

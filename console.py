#!/usr/bin/python3


'''Module'''

import cmd
import json
import os
import uuid
from datetime import datetime


class BaseModel:
    '''Class'''

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


class FileStorage:
    '''Class'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    class_name = obj['__class__']
                    self.new(eval(class_name)(**obj))


# Define new classes here
class Place(BaseModel):
    '''Class'''
    pass


class State(BaseModel):
    '''Class'''
    pass


class City(BaseModel):
    '''Class'''
    pass


class Amenity(BaseModel):
    '''Class'''
    pass


class Review(BaseModel):
    '''Class'''
    pass


storage = FileStorage()
storage.reload()


class HBNBCommand(cmd.Cmd):
    '''Class'''

    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "Place", "State", "City",
                         "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        if arg and arg not in ["BaseModel", "Place", "State", "City",
                               "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            obj_list = [str(obj) for obj in storage.all().values()
                        if not arg or obj.__class__.__name__ == arg]
            print(obj_list)

    def do_update(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

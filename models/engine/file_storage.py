#!/usr/bin/python3
"""the file storage mechanism"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    def __init__(self, file_path):
        self.__file_path = file_path  # Path to the JSON file
        self.__objects = {}  # Dictionary to store objects

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f, default=lambda x: x.__dict__)

    def reload(self):
    try:
        with open(FileStorage.__file_path) as f:
            objdict = json.load(f)
            for obj_key, obj_data in objdict.items():
                cls_name = obj_data["__class__"]
                if cls_name in globals():
                    obj = globals()[cls_name](**obj_data)
                    self.new(obj)
                else:
                    # Handle cases where the class is not defined
                    print(f"Unknown class '{cls_name}' encountered in JSON file.")
    except FileNotFoundError:
        # Create an empty storage if the file doesn't exist
        self.__objects = {}


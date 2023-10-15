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

class FileStorage():
    def __init__(self, file_path):
        self.__file_path = "file_path"  # Path to the JSON file
        self.__objects = {}  # Dictionary to store objects
        
    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = "models." + class_name
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
                

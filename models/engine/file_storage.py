#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """A class that performs serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        n_obj = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(n_obj, obj.id)] = obj
    
    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dctn = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(dctn, f)
    
    def reload(self):
         """ Deserializes __objects from the JSON file """
         dct = {'BaseModel': BaseModel}
         if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, val in json.load(f).items():
                    self.new(dct[val['__class__']](**val))

#!/usr/bin/python3
"""Define basemodel class"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Class Basemodel"""
    def __init__(self, *args, **kwargs):
        """Initializes a new base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(val, time_f)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)
            pass
    
    
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
    

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        name_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_class, self.id, self.__dict__)
    

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of instance"""
        my_dict = self.__dict__.copy()        
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = type(self).__name__                
        return my_dict

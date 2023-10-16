#!/usr/bin/python3
import uuid
import datetime
"""my basemodel"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def update_timestamp(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def save(self):
        self.update_timestamp()

    def __str__(self):
        gname = self.__class__.__name__
        if hasattr(self, 'name') and hasattr(self, 'my_number'):
            return "[{}] ({}) {}".format(gname, self.id, self.__dict__)
        return "[{}] ({}) {}".format(gname, self.id, self.__dict__)

#!/usr/bin/python3
import uuid
from models import storage
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.create_at

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def save(self):
        """Call the save method of storage."""
        storage.new(self)
        storage.save()

    def __str__(self):
        gname = self.__class__.__name__
        if hasattr(self, 'name') and hasattr(self, 'my_number'):
            return "[{}] ({}) {}".format(gname, self.id, self.__dict__)
        return "[{}] ({}) {}".format(gname, self.id, self.__dict__)

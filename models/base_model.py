#!/usr/bin/python3
"""
BaseModel module
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Class initialization, serialization and deserialization"""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel istance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key pairs of attributes.
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def to_dict(self):
        """Convert instance attributes to dictionary"""
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

    def save(self):
        """Update updated_at and save the object to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """String representation of the object"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

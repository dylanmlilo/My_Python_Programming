#!/usr/bin/python3
""" Defines a base model class module """
import uuid
import models
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments.

        Returns:
            None.

        Raises:
            None.
        """
        if kwargs:
            for key in kwargs:
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.fromisoformat(kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Save the object to the database.

        Parameters:
            self: The instance of the object.

        Return:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        :return: dict
            A dictionary containing the object's attributes and their values.
        """
        object_dict = self.__dict__.copy()
        object_dict["__class__"] = type(self).__name__
        object_dict["created_at"] = object_dict["created_at"].isoformat()
        object_dict["updated_at"] = object_dict["updated_at"].isoformat()
        return object_dict

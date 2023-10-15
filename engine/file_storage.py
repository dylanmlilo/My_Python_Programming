#!/usr/bin/python3
""" Defines the FileStorage class """
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Defines the FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all the objects of the class.
        """
        return self.__objects

    def new(self, obj: dict):
        """
        Adds a new object to the internal dictionary.

        Args:
            obj (dict): The object to be added.

        Returns:
            None
        """
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """
        Saves the contents of the object dictionary to a JSON file.

        Parameters:
            None

        Returns:
            None
        """
        new_dict = {}
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file)

    def reload(self):
        """
        Reloads the object state by reading from a JSON file.

        Parameters:
            None.

        Returns:
            None.
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                cls_name = key.split(".")[0]
                self.new(eval(cls_name + "(**value)"))
        except FileNotFoundError:
            pass

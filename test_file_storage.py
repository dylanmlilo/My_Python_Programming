#!/usr/bin/python3
""" Unittests for the FileStorage class """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class FileStorageTestCase(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after the test case.
        """
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """
        Testing the all() method.
        """
        object1 = BaseModel()
        object2 = User()
        self.storage.new(object1)
        self.storage.new(object2)
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn(object1, objects.values())
        self.assertIn(object2, objects.values())

    def test_new(self):
        """
        Testing the new() method.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(obj, self.storage._FileStorage__objects.values())

    def test_save(self):
        """
        Testing the save() method.
        """
        object1 = BaseModel()
        object2 = User()
        self.storage.new(object1)
        self.storage.new(object2)
        self.storage.save()


if __name__ == '__main__':
    unittest.main()

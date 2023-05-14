#!/usr/bin/python3
"""Unittest for place.py"""
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances and methods from place class"""

    plc = Place()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.plc)), "<class 'models.place.Place'>")

    def test_user_inheritance(self):
        """test if Place is a subclass of BaseModel"""
        self.assertIsInstance(self.plc, Place)
	
	def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))	

		
if __name__ == '__main__':
    unittest.main()

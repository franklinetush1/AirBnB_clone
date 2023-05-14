#!/usr/bin/python3
"""Unittest for amenity.py"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    amen = Amenity()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amen)), res)
	
	def test_one_save(self):
        sleep(0.05)
        first_updated_at = amen.updated_at
        amen.save()
        self.assertLess(first_updated_at, amen.updated_at)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amen, Amenity)
	
	def test_to_dict_contains_added_attributes(self):
        amen.middle_name = "Hank"
        amen.my_number = 46
        self.assertEqual("Hank", amen.middle_name)
        self.assertIn("my_number", amen.to_dict())
		
if __name__ == '__main__':
    unittest.main()

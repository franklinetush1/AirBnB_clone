#!/usr/bin/python3
"""Unittest for user.py"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """Tests instances and methods from user class"""

    usr = User()

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.usr)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.usr, User)
	
	def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))
	
	def test_save(self):
        sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)
	
	def test_to_dict_contains_correct_keys(self):
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())	
	
if __name__ == '__main__':
    unittest.main()

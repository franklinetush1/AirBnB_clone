#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import models
import unittest
from datetime import datetime
from models.review import Review


class Test_instantiation(unittest.TestCase):
    """Unittests for testing Review class."""
	
	rev = Review()

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())
	
	def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.rev, Review)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))
	
	def test_save(self):        
        sleep(0.05)
        first_updated_at = rev.updated_at
        rev.save()
        self.assertLess(first_updated_at, rev.updated_at)
	
	def test_to_dict_datetime_attributes_are_strs(self):
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))
		
if __name__ == '__main__':
    unittest.main()

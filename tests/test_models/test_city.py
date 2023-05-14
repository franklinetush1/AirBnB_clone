#!/usr/bin/python3
"""Defines unittests for city.py."""

import models
import unittest
from datetime import datetime
from models.city import City


class Test_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""
	cty = City()
    def test_save(self):
        sleep(0.05)
        first_updated_at = cty.updated_at
        cty.save()
        self.assertLess(first_updated_at, cty.updated_at)
	
	def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.cty, 'state_id'))
        self.assertTrue(hasattr(self.cty, 'name'))
        self.assertTrue(hasattr(self.cty, 'id'))
        self.assertTrue(hasattr(self.cty, 'created_at'))
        self.assertTrue(hasattr(self.cty, 'updated_at'))
if __name__ == '__main__':
    unittest.main()

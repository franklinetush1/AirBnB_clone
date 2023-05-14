#!/usr/bin/python3
"""Unittest for amenity.py"""
import unittest
from models.state import State
import datetime

class TestState(unittest.TestCase):
    """ Tests State class """

    ste = State()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.ste)), res)
	
	 def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.ste, State)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.ste, 'name'))
        self.assertTrue(hasattr(self.ste, 'id'))
        self.assertTrue(hasattr(self.ste, 'created_at'))
        self.assertTrue(hasattr(self.ste, 'updated_at'))
	
	def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))
	
	def test_one_save(self):
        sleep(0.05)
        first_updated_at = ste.updated_at
        ste.save()
        self.assertLess(first_updated_at, ste.updated_at)
		
if __name__ == '__main__':
    unittest.main()

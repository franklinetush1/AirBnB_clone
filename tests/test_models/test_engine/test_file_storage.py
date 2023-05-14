#!/usr/bin/python3
""" Module of Unittests """
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """ Suite of File Storage Tests """

  basem = BaseModel()
	usrid = User()
	plc = Place()
	ste = State()        
	cty = City()
	rev = Review()
	amen = Amenity()
	
	def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.basem.full_name = "BaseModel Instance"
        self.basem.save()
        bm_dict = self.basem.to_dict()
        all_objs = storage.all()

        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)
	
	def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)
	
	def test_reload(self):
	
        models.storage.new(basem)
        models.storage.new(usrid)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amen)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + basem.id, objs)
        self.assertIn("User." + usrid.id, objs)
        self.assertIn("State." + ste.id, objs)
        self.assertIn("Place." + plc.id, objs)
        self.assertIn("City." + cty.id, objs)
        self.assertIn("Amenity." + amen.id, objs)
        self.assertIn("Review." + rev.id, objs)
	
	def test_new(self):
	
        models.storage.new(basem)
        models.storage.new(usrid)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amen)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel." + basem.id, models.storage.all().keys())
        self.assertIn(basem, models.storage.all().values())
        self.assertIn("User." + usrid.id, models.storage.all().keys())
        self.assertIn(usrid, models.storage.all().values())
        self.assertIn("State." + ste.id, models.storage.all().keys())
        self.assertIn(ste, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amen.id, models.storage.all().keys())
        self.assertIn(amen, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())
	
	def test_save(self):
	
        models.storage.new(basem)
        models.storage.new(usrid)
        models.storage.new(ste)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amen)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + basem.id, save_text)
            self.assertIn("User." + usrid.id, save_text)
            self.assertIn("State." + ste.id, save_text)
            self.assertIn("Place." + plc.id, save_text)
            self.assertIn("City." + cty.id, save_text)
            self.assertIn("Amenity." + amen.id, save_text)
            self.assertIn("Review." + rev.id, save_text)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Test the BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instance_attributes(self):
        """
        Create a new instance of BaseModel and verify that the
        id, created_at and updated_at attributes are set correctly.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save_method(self):
        """
        Call the save() method on a BaseModel
        instance and verify that the updated_at
        attribute is updated with the current datetime.
        """
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        Call the to_dict() method on a BaseModel
        instance and verify that the returned dictionary
        contains the correct keys and values.
        """
        base_model = BaseModel()
        my_dict = base_model.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIn('__class__', my_dict)
        self.assertIn('created_at', my_dict)
        self.assertIn('updated_at', my_dict)
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(my_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'],
                         base_model.updated_at.isoformat())

    def test_invalid_attributes(self):
        """
        Create a new instance of BaseModel
        and manually set the id, created_at
        and updated_at attributes to invalid values.
        Verify that no exception is raised.
        """
        base_model = BaseModel()
        base_model.id = 123
        base_model.created_at = '2022-01-01'
        base_model.updated_at = '2022-01-01'
        self.assertEqual(base_model.id, 123)
        self.assertEqual(base_model.created_at, '2022-01-01')
        self.assertEqual(base_model.updated_at, '2022-01-01')

    def test_str_method(self):
        """
        Create a new instance of a subclass of BaseModel
        and verify that the __str__() method
        returns the correct string representation.
        """
        class SubModel(BaseModel):
            pass
        sub_model = SubModel()
        expected_str = "[SubModel] ({}) {}".format(
            sub_model.id, sub_model.__dict__)
        self.assertEqual(str(sub_model), expected_str)


if __name__ == '__main__':
    unittest.main()

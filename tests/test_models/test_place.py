#!/usr/bin/python3
"""Module for test Place class"""
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import models


class TestPlace(unittest.TestCase):
    """create a new instance of place
    and verify it is an instance of BaseModel"""

    def test_create_instance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)

    """create a new place with valid attributes"""

    def test_create_place_with_valid_details(self):
        place = Place()
        place.name = "test@example.com"
        place.state_id = "password123"

        self.assertEqual(place.name, "test@example.com")
        self.assertEqual(place.state_id, "password123")

    """update place's attributes"""

    def test_update_place_details(self):
        place = Place()
        place.email = "test@example.com"
        place.password = "password123"
        place.first_name = "John"
        place.last_name = "Doe"
        place.email = "new@example.com"
        place.password = "newpassword123"
        place.first_name = "Jane"
        place.last_name = "Smith"
        self.assertEqual(place.email, "new@example.com")
        self.assertEqual(place.password, "newpassword123")
        self.assertEqual(place.first_name, "Jane")
        self.assertEqual(place.last_name, "Smith")

    """save place's data to storage"""

    def test_save_place_data_to_storage(self):
        place = Place()
        place.email = "test@example.com"
        place.password = "password123"
        place.first_name = "John"
        place.last_name = "Doe"
        place.save()

    """create a new place with empty attributes """

    def test_create_place_with_empty_details(self):
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.amenity_ids, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.name, "")
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.number_rooms, 0)


if __name__ == "__main__":
    unittest.main()

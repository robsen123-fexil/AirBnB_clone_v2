#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel

from models.place import Place




class TestPlace(TestBasemodel):
    """Represents odel."""
    def __init__(self, *args, **kwargs):
        """Initializ class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place



    def test_city_id(self):
        """Tests the type of d."""
        new = self.value()
        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_user_id(self):
        """Tests the """
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_name(self):
        """Tests  name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_description(self):
        """Tests the """
        new = self.value()
        self.assertEqual(
            type(new.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_number_rooms(self):
        """Tests the ."""
        new = self.value()
        self.assertEqual(
            type(new.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_number_bathrooms(self):
        """Tests ooms."""
        new = self.value()
        self.assertEqual(
            type(new.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )





    def test_max_guest(self):
        """Tests thst."""
        new = self.value()
        self.assertEqual(
            type(new.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
      
      
        )





    def test_price_by_night(self):
        """Tests y_night."""
        new = self.value()
        self.assertEqual(
            type(new.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_latitude(self):
        """Tetitude."""
        new = self.value()
        self.assertEqual(
            type(new.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )




    def test_longitude(self):
        """Tests tngitude."""
        new = self.value()
        self.assertEqual(
            type(new.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )





    def test_amenity_ids(self):
        """Tesmenity_ids."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

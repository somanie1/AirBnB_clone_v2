#!/usr/bin/python3
"""Amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test for Attribute Amenity """

    def __init__(self, *args, **kwargs):
        """ Instanstiation  """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Tests for name of amenity """
        new = self.value()
        new.name = "gym"
        self.assertEqual(type(new.name), str)

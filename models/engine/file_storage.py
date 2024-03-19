#!/usr/bin/python3

import json
import os
from importlib import import_module


class FileStorage:
    """Th"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """"""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,'User': import_module('models.user').User,'State': import_module('models.state').State,'City': import_module('models.city').City,'Amenity': import_module('models.amenity').Amenity,'Place': import_module('models.place').Place,'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

    def delete(self, obj=None):
        """"""
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """Saves  file"""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads  file"""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)

    def close(self):
        """Cengine."""
        self.reload()

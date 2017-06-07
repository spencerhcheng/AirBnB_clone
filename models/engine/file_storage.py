#!/usr/bin/python3
import json
import datetime

class FileStorage:
    def __init__(self):
        self.__file_path = './file.json'
        self.__objects = {}

    def all(self):
        obj = self.reload()
        return obj

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        store = {}
        obj = self.__objects
        for i in self.__objects.keys():
            temp = self.__objects[i].to_json()
        store[i] = temp
        with open(self.__file_path, 'w+') as f:
            json.dump(store, f)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            r = json.load(f)
        from models.base_model import BaseModel
        for i in r.keys():
            self.__objects[i] = BaseModel(r[i])
        return self.__objects

        """
        self.__objects[i] = eval(BaseModel)(r[i])
        """

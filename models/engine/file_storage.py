#!/usr/bin/python3
import json
import datetime
import os.path

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
        for i in self.__objects.keys():
            temp = self.__objects[i].to_json()
            store[i] = temp
        with open(self.__file_path, 'w+') as f:
            json.dump(store, f)

    def reload(self):
        if (os.path.exists(self.__file_path)):
            with open(self.__file_path, 'r') as f:
                r = json.load(f)
            from models.base_model import BaseModel
            from models.user import User

            for i in r.keys():
                if r[i]["__class__"] == "BaseModel":
                    self.__objects[i] = BaseModel(**r[i])
                if r[i]["__class__"] == "User":
                    self.__objects[i] = User(**r[i])
            return self.__objects
        else:
            return {}

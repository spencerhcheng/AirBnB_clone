#!/usr/bin/python3
import json

class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        obj = self.reload()
        """
        return self.__objects
        """
        return obj

    def new(self, obj):
        self.__objects = obj

    def save(self):
        d = self.__objects
        print(d)
        """
        js = {}
        id = d['_FileStorage__objects']['id']
        js[id] = d['_FileStorage__objects']
        print(js)
        with open("file.json", 'w') as f:
            json.dump(obj, f)
        """
    def reload(self):
        try:
            with open("file.json", 'r') as f:
                rd = json.load(f)
        except ValueError:
            return {}
        return rd

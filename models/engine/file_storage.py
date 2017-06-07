#!/usr/bin/python3
import json
import datetime
class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        obj = self.reload()
        return obj

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        new_json = {}
        new_dict = {}
        obj = self.__objects
        for k, v in obj.items():
            id = k
            cls = v.__class__.__name__
            new_dict = obj[k].__dict__
        new_json[id] = new_dict
        new_dict.update({'__class__': cls})
        for k, v in new_json[id].items():
            if isinstance(v, datetime.datetime):
                new_dict.update({k : str(v)})
            else:
                new_dict.update({k : v})
        new_json[id] = new_dict
        with open(self.__file_path, 'w') as f:
            json.dump(new_json, f)

    def reload(self):
        with open("file.json", 'r') as f:
            rd = json.load(f)

        print("hi ---------")
        print(rd)
        
        return {"hello" : "world"}

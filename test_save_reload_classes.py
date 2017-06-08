#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.amenity import Amenity
from models.city import City
all_objs = storage.all()
print("---Reloaded objects---")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Creating a new state ---")
my_state = State()
my_state.name = "California"
print(my_state)

print("-- Creating Amenities ---")
my_amenities = Amenity()
print(my_amenities)



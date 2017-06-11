# Air BnB Clone

This is a command interpreter to manage AirBnB objects. This is the first step towards building your full web application: the AirBnB clone. 

## Environment
Our Monty interpreter has been tested on Ubuntu 14.05.5 LTS

Tests done in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)

## Repository Breakdown
Once cloned over, the repository will contain the following files:

|   **File**    |  **Decription**                       |
|---------------|---------------------------------------|
| console.py   | contains the entry point of the command interpreter           |
| init_test.sh      | runs all the test files from tests folder        |
| models/__init__.py | creates an instance of FileStorage |
| models/amenity.py | class Amenity, inherits from BaseModel |
| models/base_model.py | class BaseModel that defines all common attributes/methods for other classes |
| models/city.py | class City, inherits from BaseModel |
| models/place.py | class Place, inherits from BaseModel |
| models/review.py | class Review, inherits from BaseModel |
| models/state.py | class State, inherits from BaseModel |
| models/user.py | class User, inherits from BaseModel |
| models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
| tests/amenity_test.py | tests Amenity class |
| tests/basemodel_test.py | tests BaseModel class |
| tests/city_test.py | tests City class |
| tests/place_test.py | tests Place class |
| tests/review_test.py | tests Review class |
| tests/state_test.py | tests State class |
| tests/user_test.py | tests User class |

## Description of Classes
1. [models/amenity.py](models/amenity.py) - Class Amenity, inherits from BaseModel
  * ``name`` - public class attribute
2. [models/base_model.py](models/base_model.py) - Class BaseModel that defines all common attributes/methods for other classes
  * ``dt_format`` - public class attribute that defines format of the date and time
  * ``id`` - public instance attribute, assigned with an uuid when an instance is created
  * ``created_at`` - public instance attribute, datetime - assigned with the current datetime when an instance is created
  * ``updated_at`` - public instance attribute, datetime - assigned with the current datetime when an instance is updated
  * ``save`` - public instance method that updates the public instance attribute updated_at with the current datetime
  * ``to_json`` - public instance method that returns a dictionary containing all keys/values of __dict__ of the instance + the class name in the key __class__
3. [models/city.py](models/city.py) - Class City, inherits from BaseModel
  * ``state_id`` - public class attribute: it will be the State.id
  * ``name`` - public class attribute
4. [models/place.py](models/place.py) - Class Place, inherits from BaseModel
  * ``city_id`` - public class attribute: it will be the City.id
  * ``user_id`` - public class attribute: it will be the User.id
  * ``name`` - public class attribute
  * ``description`` - public class attribute
  * ``number_rooms`` - public class attribute
  * ``number_bathrooms`` - public class attribute
  * ``max_guest`` - public class attribute
  * ``price_by_night`` - public class attribute
  * ``latitude`` - public class attribute
  * ``longitude`` - public class attribute
  * ``amenity_ids`` - public class attribute: it will be the list of Amenity.id
5. [models/review.py](models/review.py) - Class Review, inherits from BaseModel
  * ``place_id`` - public class attribute: it will be the Place.id
  * ``user_id`` - public class attribute: it will be the User.id
  * ``text`` - public class attribute
6. [models/state.py](models/state.py) - Class State, inherits from BaseModel
  * ``name`` - public class attribute
7. [models/user.py](models/user.py) - Class User, inherits from BaseModel
  * ``email`` - public class attribute
  * ``password`` - public class attribute
  * ``first_name`` - public class attribute
  * ``last_name`` - public class attribute
8. [models/engine/file_storage.py](models/engine/file_storage.py) - Class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances
  * ``__file_path`` - private class attribute; path to the JSON file
  * ``__objects`` - private class attribute; empty but will store all objects by <class name>.id
  * ``all`` - public instance method; returns __objects
  * ``new`` - public instance method; sets in __objects the obj with key <obj class name>.id
  * ``save`` - public instance method; serializes __objects to the JSON file
  * ``reload`` - public instance method; deserializes the JSON file to __objects

## How to Use
First step is to clone the repository into your directory
```
$ git clone https://github.com/lisale0/AirBnB_clone

## Example of Use
Run the executable `./console.py`
```
vagrant@vagrant$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show

(hbnb) create City
4af7890c-007f-42ff-97d8-074214f1094f
(hbnb) show City 4af7890c-007f-42ff-97d8-074214f1094f
[City] (4af7890c-007f-42ff-97d8-074214f1094f) {'id': '4af7890c-007f-42ff-97d8-074214f1094f', 'updated_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679386), '__class__': 'City', 'created_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679362)}
(hbnb)$
```
## Notes
Other functionalities are currently in development.

## Known Bugs
coming soon

### Authors
*Lisa Leung* - [Github](https://github.com/lisale0) || [Twitter](https://twitter.com/lisale01) || [email](lisa.leung@holbertonschool.com)

*Spencer Cheng* - [Github](https://github.com/spencerhcheng) || [Twitter](https://twitter.com/spencerhcheng) || [email](spencer.cheng@gmail.com)

*Julija Lee* - [Github](https://github.com/FreeJules) || [Twitter](https://twitter.com/LeeJulija) || [email](julijalee@gmail.com)


#### Feedback and contributors welcomed. Reach out to either authors.

#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

"""module: console.py"""


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_create(self, args):
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if s[0] is None:
                print("** class name missing **")
            else:
                if s[0] in classes:
                    cls = classes[s[0]]()
                    cls.save()
                else:
                    print("** class doesn't exist **")
    def do_show(self, args):
        if not args:
            print("** class name missing **")
        else:
            s = args.split()

            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                    print(obj[s[1]])
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                if s[0] in classes:
                    obj = storage.all()
                else:
                    print("** class doesn't exist **")
    def emptyline(self):
        pass

if __name__ == '__main__':
    classes = {'BaseModel': BaseModel}
    HBNBCommand().cmdloop()

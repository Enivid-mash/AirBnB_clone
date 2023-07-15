#!/usr/bin/python3
"""This class defines the entry point for the command interpretter"""
import cmd
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Represents the hbnb console"""
    prompt = "(hbnb) "
    the_classes = {"BaseModel", "User", "City", "State", "Place", "Amenity", "Review"}

    def emptyline(self):
        """This ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quits command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quits command to exit the program at the end of file"""
        print("")
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to the
        JSON file
        Exceptions:
        SyntaxError: when there is no args provided
        NameError: absence of an object
        """
        try:
            if not line:
                raise SyntaxError()
            the_list = line.split(" ")
            obj = eval("{}()".format(the_list[0]))
            print("{}".format(obj.id))
            for num in range(1, len(the_list)):
                the_list[num] = the_list[num].replace('=', ' ')
                attr = split(the_list[num])
                attr[1] = attr[1].replace('-', ' ')
                try:
                    vari = eval(attr[1])
                    attr[1] = vari
                except ValueError:
                    pass
                if type(attr[1]) is not tuple:
                    setattr(obj, attr[0], attr[1])
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """prints the string representation of an instance
        based on the class name and id
        Exceptions:
        SyntaxError: absence of a class name
        NameError:class name doesn't exist
        IndexError:instance id missing
        KeyError: no instance found
        """
        try:
            if not line:
                raise SyntaxError()
            the_list = line.split(" ")
            if the_list[0] not in self.the_classes:
                raise NameError()
            if len(the_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = the_list[0] + '.' + the_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exception:
        SyntaxError:when class name is missing
        NameError: class name doesn't exist
        IndexError: instance id not given
        KeyError:no valid id provided
        """
        try:
            if not line:
                raise SyntaxError()
            the_list = line.split(" ")
            if the_list[0] not in self.the_classes:
                raise NameError()
            if len(the_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = the_list[0] + '.' + the_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        Exceptions:
        NameError: There is no object with that name
        """
        if not line:
            obj = storage.all()
            print([obj[k].__str__() for k in obj])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.the_classes:
                raise NameError
            obj = storage.all(eval(args[0]))
            print([obj[k].__str__() for k in obj])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance by adding or updating attribute
        Exceptions:
            SyntaxError: when there is no args provided
            NameError: There is no object that has the name
            IndexError: when there is no id given
            KeyError: There is no valid id given
            AttributeError: when there is no attribute given
            ValueError: no value provided
        """
        try:
            if not line:
                raise SyntaxError()
            the_list = split(line, " ")
            if the_list[0] not in self.the_classes:
                raise NameError()
            if len(the_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = the_list[0] + '.' + the_list[1]
            if key not in objects:
                raise KeyError()
            if len(the_list) < 3:
                raise AttributeError()
            if len(the_list) < 4:
                raise ValueError()
            val = objects[key]
            try:
                val.__dict__[the_list[2]] = eval(the_list[3])
            except Exception:
                val.__dict__[the_list[2]] = the_list[3]
                val.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** no instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing**")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

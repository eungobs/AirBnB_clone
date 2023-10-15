#!/usr/bin/python3
"""
Console module for BaseModel.
"""

import cmd
from models.base_model import BaseModel
from io import StringIO
from unittest.mock import patch

# Import your additional model classes (Place, State, City, Amenity, Review) here
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # Add new classes to the BaseModel.class_dict
    BaseModel.class_dict['Place'] = Place
    BaseModel.class_dict['State'] = State
    BaseModel.class_dict['City'] = City
    BaseModel.class_dict['Amenity'] = Amenity
    BaseModel.class_dict['Review'] = Review

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id."""
        class_name = arg.strip()
        if not class_name:
            print("** class name missing **")
        elif class_name not in BaseModel.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel.class_dict[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and ID."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                instances = BaseModel.class_dict[class_name].all()
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                instances = BaseModel.class_dict[class_name].all()
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    del instances[key]
                    BaseModel.save_to_file()
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

    def do_all(self, arg):
        """Print all string representations of instances of a class."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        else:
            try:
                instances = BaseModel.class_dict[args[0]].all()
                print([str(instance) for instance in instances.values()])
            except Exception as e:
                print(e)

    def do_count(self, arg):
        """Retrieve and print the number of instances of a class."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        else:
            try:
                instances_count = BaseModel.class_dict[args[0]].count()
                print(instances_count)
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """Update an instance based on the class name, ID, attribute name, and attribute value."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            try:
                instances = BaseModel.class_dict[class_name].all()
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    instance = instances[key]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

    def do_show(self, arg):
        """Show the string representation of an instance based on the class name and ID."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                instances = BaseModel.class_dict[class_name].all()
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """Update an instance based on the class name, ID, and a dictionary representation."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in BaseModel.class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** dictionary representation missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            try:
                instances = BaseModel.class_dict[class_name].all()
                key = "{}.{}".format(class_name, instance_id)
                if key in instances:
                    obj = instances[key]
                    try:
                        dictionary = eval(' '.join(args[2:]))
                        if type(dictionary) == dict:
                            for k, v in dictionary.items():
                                if k not in ['id', 'created_at', 'updated_at']:
                                    setattr(obj, k, v)
                            obj.save()
                        else:
                            print("** Invalid dictionary representation **")
                    except:
                        print("** Invalid dictionary representation **")
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

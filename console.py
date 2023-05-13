#!/usr/bin/python3
"""Command interpreter module."""
import cmd
from models import storage
import shlex
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __default_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""        
        return True  
    
    def do_create(self, input):
        """ Creates an instance according to a given class """

        if not input:
            print("** class name missing **")
        elif input not in HBNBCommand.__default_classes:
            print("** class doesn't exist **")
        else:
            dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'City': City, 'Amenity': Amenity, 'State': State,
                   'Review': Review}
            instance = dict[input]()
            print(instance.id)
            instance.save()
    

    def do_destroy(self, input):
        """Deletes an instance based on the class name and id"""
        if input == "" or input is None:
            print("** class name missing **")
        else:
            input1 = input.split(' ')
            if input1[0] not in HBNBCommand.__default_classes:
                print("** class doesn't exist **")
            elif len(input1) == 1:
                print("** instance id missing **")
            else:
                indx = "{}.{}".format(input1[0], input1[1])
                if indx not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[indx]
                    storage.save()
    
    def do_show(self, imput):
        """Print string representation of an instance"""
        if imput == "" or imput is None:
            print("** class name missing **")
        else:
            imput1 = imput.split(' ')
            if imput1[0] not in HBNBCommand.__default_classes:
                print("** class doesn't exist **")
            elif len(imput1) == 1:
                print("** instance id missing **")
            else:
                indx = "{}.{}".format(imput1[0], imput1[1])
                if indx not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[indx])
    

    def do_all(self, input):
        """Prints all string representation"""
        if input != "":
            input1 = input.split(' ')
            if input1[0] not in HBNBCommand.__default_classes:
                print("** class doesn't exist **")
            else:
                list1 = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == input1[0]]
                print(list1)
        else:
            list2 = [str(obj) for key, obj in storage.all().items()]
            print(list2)

    def do_update(self, input):
        """ Updates an instance"""

        if not input:
            print("** class name missing **")
            return

        brk = ""
        for i in input.split(','):
            brk += i
        input1 = shlex.split(brk)
        if input1[0] not in HBNBCommand.__default_classes:
            print("** class doesn't exist **")
        elif len(input1) == 1:
            print("** instance id missing **")
        else:
            all_instances = storage.all()
            for key, instance in all_instances.items():
                inst_name = instance.__class__.__name__
                inst_id = instance.id
                if inst_name == input1[0] and inst_id == input1[1].strip('"'):
                    if len(input1) == 2:
                        print("** attribute name missing **")
                    elif len(input1) == 3:
                        print("** value missing **")
                    else:
                        setattr(instance, input1[2], input1[3])
                        storage.save()
                    return
            print("** no instance found **")  


if __name__ == '__main__':
    HBNBCommand().cmdloop()

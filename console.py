#!/usr/bin/python3
"""The console for AirBnB project
"""


import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        "Create a new instance of BaseModel"
        if not arg:
            print("** class name missing **")
            return False
        elif arg.split()[0] not in ['BaseModel', 'User', 'Place', 'State',
                                    'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return False

        if arg.split()[0] == 'BaseModel':
            obj = eval(f"models.base_model.{arg}()")
        elif arg.split()[0] == 'User':
            obj = eval(f"models.user.{arg}()")
        elif arg.split()[0] == 'Place':
            obj = eval(f"models.place.{arg}()")
        elif arg.split()[0] == 'State':
            obj = eval(f"models.state.{arg}()")
        elif arg.split()[0] == 'City':
            obj = eval(f"models.city.{arg}()")
        elif arg.split()[0] == 'Amenity':
            obj = eval(f"models.amenity.{arg}()")
        elif arg.split()[0] == 'Review':
            obj = eval(f"models.review.{arg}()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        "Prints the string representation of an instance"
        values = arg.split()
        if not arg:
            print("** class name missing **")
            return False
        elif values[0] not in ['BaseModel', 'User', 'Place', 'State',
                               'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return False
        elif len(values) == 1:
            print("** instance id missing **")
            return False

        all_objs = models.storage.all()
        for obj in all_objs.values():
            if obj.id == values[1]:
                print(obj)
                return False
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        "Deletes an instance based on the class name and id"
        values = arg.split()
        if not arg:
            print("** class name missing **")
            return False
        elif values[0] not in ['BaseModel', 'User', 'Place', 'State',
                               'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return False
        elif len(values) == 1:
            print("** instance id missing **")
            return False

        all_objs = models.storage.all()
        for k, v in all_objs.items():
            if v.id == values[1]:
                all_objs.pop(k)
                models.storage.save()
                return False
        else:
            print("** no instance found **")

    def do_all(self, arg):
        "Prints all string representation of all instances"
        values = arg.split()
        if len(values) == 0:
            list_ = [f"{v}" for v in models.storage.all().values()]
            print(list_)
        elif len(values) == 1:
            list_ = [f"{v}"
                     for v in models.storage.all().values()
                     if v.__class__.__name__ == values[0]]
            if not list_:
                print("** class doesn't exist **")
                return False
            else:
                print(list_)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        values = arg.split()
        if not values:
            print("** class name missing **")
            return False
        if values[0]:
            flag = 0
            for v in models.storage.all().values():
                if v.__class__.__name__ == values[0]:
                    flag = 1
                    break
            if not flag:
                print("** class doesn't exist **")
                return False
            elif len(values) == 1:
                print("** instance id missing **")
                return False
        if values[1]:
            flag = 0
            for v in models.storage.all().values():
                if v.id == values[1]:
                    flag = 1
                    break
            if not flag:
                print("** no instance found **")
                return False
            elif len(values) == 2:
                print("** attribute name missing **")
                return False
        if values[2]:
            if len(values) == 3:
                print("** value missing **")
                return False
        all_objs = models.storage.all()
        for v in all_objs.values():
            if v.id == values[1] and v.__class__.__name__ == values[0]:
                setattr(v, values[2], values[3].strip('"'))
                break

    def do_quit(self, arg):
        "Quit command to exit the program"
        print()
        return True

    def do_EOF(self, arg):
        """Capture EOF (Ctrl + D)"""
        print("Exiting...")
        return True

    def postcmd(self, stop, line):
        """Execute after processing each command"""
        if line == 'EOF' or line == 'quit':
            return True
        self.lastcmd = ""


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""The console for AirBnB project
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        """Capture EOF (Ctrl + D)"""
        print("Exiting...")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

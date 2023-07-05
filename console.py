#!/usr/bin/python3
"""The console for AirBnB project
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    intro = "Welcome to the command interpreter for AirBnB clone"
    prompt = "(hbnb) "

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
        if line == 'EOF':
            return True
        self.lastcmd = ""


if __name__ == '__main__':
    HBNBCommand().cmdloop()

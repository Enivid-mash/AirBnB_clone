#!/usr/bin/python3
"""This class defines the entry point for the command interpretter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Represents the hbnb console"""
    prompt = "(hbnb) "

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

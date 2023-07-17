# AirBnB clone - The console
                                    (hbnb)
#### This is a command interpreter for managing objects on our airbnb project.
#### This console will create the data model, manage, that is create, update, destroy objects and store and persist objects to a file(JSON)

#### To start the console, use the (cd) command which changes, the directory to the project folder and execute or run it by typing this on your terminal ./console.py

#### After running the ./console.py there will be a (hbnb) prompt where you will type in your commands, for example our supported commands are:

+ `help` - displays descriptions of all the supported commands

+ `create` - command that creates an object

+ `show` - command that shows an object based on id

+ `destroy` - command that destroys an object

+ `all` - command that displays all the objects either of one or all types

+ `quit/EOF` - EOF means end of file - This command quits the console.

### Examples of commands:
```
(hbnb) help for example (hbnb) help

(hbnb) create <classname> for exampe (hbnb) create BaseModel

(hbnb) show <classname><object id> for exampe (hbnb) show User my_id

(hbnb) destroy <classname><object id> for exampe (hbnb) destroy City my_city_id

(hbnb) all <classname> for exampe (hbnb) all State

(hbnb) quit for exampe (hbnb) quit or EOF
```

### The supported classes are:

+ BaseModel - This is the base class of all the classes whereby the rest of the classes will inherit from it.

+ User

+ State

+ City

+ Place

AirBnB Clone Project
Project Description
This project is an implementation of a simplified version of the AirBnB web application. The goal is to build a command-line interpreter that manages various AirBnB objects, including users, states, cities, places, amenities, and reviews. The project utilizes a parent class (BaseModel) for object initialization, serialization, and deserialization. Additionally, it introduces a file storage system for storing and retrieving instances.

Command Interpreter
The command interpreter allows users to perform various operations on AirBnB objects through a shell-like interface. Key functionalities include:

Creating new objects (e.g., User, Place).
Retrieving objects from a file or database.
Performing operations on objects (e.g., counting, computing stats).
Updating attributes of an object.
Destroying an object.
How to Start
To start the command interpreter, execute the console.py script:

bash
Copy code
./console.py
How to Use
Once in interactive mode, the prompt will be (hbnb). Users can enter various commands to interact with AirBnB objects. The available commands include:

create: Create a new object.
show: Show the string representation of an object.
all: Show all instances of a class or all instances in general.
destroy: Destroy an object based on the class name and id.
update: Update an object based on the class name and id.
Examples
Interactive Mode:

bash
Copy code
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678
(hbnb) all
(hbnb) destroy User 1234-5678
(hbnb) update User 1234-5678 name "John Doe"
(hbnb) quit
Non-Interactive Mode:

bash
Copy code
$ echo "create Place" | ./console.py
$ cat test_commands
show Place 1234-5678
all
destroy Place 1234-5678
update Place 1234-5678 name "New Name"
quit
$ cat test_commands | ./console.py
Authors
This project is maintained by the following contributors:

Lesego Phuku

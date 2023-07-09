# AirBnB clone - The console

![](https://res.cloudinary.com/djvwjnzxw/image/upload/v1688789698/airbnb-holberton_mx2ss7.png)
## Table of Contents

- [AirBnB clone - The console](#airbnb-clone---the-console)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Technical concepts](#technical-concepts)
    - [unittest](#unittest)
    - [\*args and \*\*kwargs](#args-and-kwargs)
    - [packages](#packages)
    - [serialization - deserialization](#serialization---deserialization)
    - [cmd](#cmd)
    - [circular import](#circular-import)
    - [modules](#modules)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Files and Directories](#files-and-directories)
  - [Authors](#authors)

## Description

This is the first part of a big project to create a clone of AirBnB. This part of the project is called **The console**. In this project we will cover the basic implementations that will build a complete clone of the AirBnB web page. Before we explain how to run and how to install this project, we will explain some concepts that will help you understand the flow of the classes (packages, modules, circular imports, etc).

## Technical concepts

These concepts are very important. You need to understand them or at least have a general understanding about how they work and how they are applied.
### unittest
This Python's module is a testing framework that allows us to write test cases. It provides a set of classes, methods and assertions to verify if our code works as expected. To work with this module we need to import it `import unittest`

```python
import unittest

class TestExample(unittest.TestCase):
  """Some useful comment"""

  def test_example(self):
    """Some useful comment"""
```

### *args and **kwargs
*args is used to pass a variable number of positional arguments to a function. The passed arguments are collected in a tuple inside the function.
```python
def function(*args):
    for arg in args:
        print(arg)

function(1, 2, 3, 4)
```

**kwargs is used to pass a variable number of keyword arguments to a function. The passed arguments are collected in a dictionary inside the function.
```python
def function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

function(name="John", age=30)
```
### packages
In Python, a package is a special folder or directory that contains related modules and the __init__.py file that indicates that the folder is a package, and initializes and defines the behavior of the package.
```bash
my_package/
	__init__.py
	module_1.py
	module_2.py
```
### serialization - deserialization
Serialization: Serialization is the process of converting an object or data structure into a stream of bytes for storage or transmission.

Deserialization: Deserialization is the reverse process of serialization.
```python
import json

# Data
data = {'nombre': 'Juan','edad': 30}

# Serialization to JSON
data_serial = json.dumps(data)

# Deserialization from JSON
data_deserial = json.loads(data_serial)

```

### cmd
In Python, cmd is a module that allows you to create an interactive command line interface.
```python
import cmd

class Console(cmd.Cmd):
	"""code"""

# Function that starts an interactive console command loop
Console().cmdloop()
```
### circular import
Circular import occurs when two or more modules import each other, creating a circular dependency. This will raise an exception called `ImportError`.
```python
# module_a.py

from module_b import b

a = 'a'
a = b

# module_b.py

from module_a import a

b = 'b'
```
### modules
In Python, a module is a file that contains reusable Python code (classes, functions, variables).
```python
""" Import math module"""

import math
result = math.sqrt(25)

# or

from math import sqrt
resultado = sqrt(25)
```

## Installation
+ The first step to get this repo is cloning it:
```bash
git clone https://github.com/xiayudev/holbertonschool-AirBnB_clone.git
```
+ After that, go into the directory:
```bash
cd ./holbertonschool-AirBnB_clone
```
+ Once there, make sure to give execution permissions to the console:
```bash
chmod u+x console.py # Add sudo at the beginning if needed
```
## Usage
There are two ways of using our console. When I say console I mean the command interpreter that allows us to create, destroy, store, etc, data (instances).
+ Interactive mode
```bash
python3 console.py
```
or
```bash
./console.py
```
+ Non-interactive mode
```bash
$ cat test_file
$ help
$ cat test_file | ./console.py
```

## Examples
Some examples using the console for creating, destroying data
+ Interactive mode
![](https://res.cloudinary.com/djvwjnzxw/image/upload/v1688928270/WhatsApp_Image_2023-07-09_at_13.39.24_ihykm0.jpg)
+ Non-interactive mode
```bash
$ cat test_file
$ create BaseModel
$ cat test_file | ./console.py
(hbnb) e630f3eb-756b-4a2b-9aa4-6b031a44fffe
(hbnb) Exiting ...
$
```
## Files and Directories
| File | Description |
| ------------ | ------------ |
| `console.py` | The command interpreter to work with |
| `models/engine/file_storage.py` | Make data persistance on a file|
| `models/base_model.py` | The base model class |
| `models/__init__.py` | Serve as a engine of the project |

| Directory | Description |
| ------------ | ------------ |
| `tests/` | All the files to be tested |
| `models/` | Important classes of the project |
## Authors

+ Josue Cerrón [@xiayudev](https://github.com/xiayudev)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://xiayudevsportfoliov2.netlify.app/) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jctuesta94/) [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/J7Jeo) [![medium](https://img.shields.io/badge/medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@josce7)
+ Sharif Abuhadba [@SharifAli645](https://github.com/SharifAli645)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/sh-abh-bts) [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/PandemiaOnirica) [![medium](https://img.shields.io/badge/medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@pandemiaonirica)

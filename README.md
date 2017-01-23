# CIn - C-like input functions for Python.

CIn is a small single-file Python module which provides methods for getting buffered input from stdin. The advantage of using CIn is that it allows you to input single chars, **unget or unread a string**, get individual int or float numbers, etc. The file is very small and can be read even by beginners to understand how it works.

**Note: It works only with Python 3. If you want Python 2 support replace input with raw_input in the cin.py file.**

## Installation

Just copy/move the cin.py file to a place from where you can import it.

## Usage

Import cinput from cin and call the methods you want to use. In case of an error, CInException is raised. Simple!
You can find an example program written in Python using CIn here: https://github.com/abhishekkr200802/evalisp

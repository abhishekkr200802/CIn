# CIn - C-like input functions for Python.

CIn is a small single-file Python module which provides methods for getting buffered input from stdin. The advantage of using CIn is that it allows you to input single chars, **unget or unread a string**, get individual int or float numbers, etc. The file is very small and can be read even by beginners to understand how it works.

**Note: It works only with Python 3. If you want Python 2 support replace input with raw_input in the cin.py file.**

## Installation

Just copy/move the cin.py file to a place from where you can import it.

## Usage

Import cinput from cin and call the methods you want to use. In case of an error, CInException is raised. Simple!
Below is me playing with cinput:

```python
>>> from cin import cinput
>>> cinput.getc()
Kill 'em with success, bury 'em with a smile.
'K'
>>> cinput.ungetc('K')
>>> cinput.getc()
'K'
>>> cinput.getc()
'i'
>>> cinput.getc()
'l'
>>> cinput.getc()
'l'
>>> cinput.empty_buffer()
["'em", 'with', 'success,', 'bury', "'em", 'with', 'a', 'smile.']
>>> cinput.getint()
123
123
>>> cinput.getfloat()
43.23
43.23
>>> cinput.getfloat()
73492739
73492739.0
```

'''
The cin module implements C-style buffered input functions. Please note that
functions like scanf, fscanf, sscanf, etc. are not present and the aim is not
to mimic C's stdio. Rather, the module implements input method which allow
the user to input single bytes at a time, uget read bytes, input
different data types, etc.

Copyright 2017 Abhishek Kumar. This module is distributed under the terms of
the GNU GPL version 3 or a newer version.

 This module is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

class CIn:
    '''Implements methods that can be used for buffered input.'''

    def __init__(self):
        self.buffer = []

    def getc(self):
        '''Read and return a single non-whitespace byte.'''

        self.fill_buffer()

        word = self.buffer[0]
        byte = word[0]
        if word[1:]:
            self.buffer[0] = word[1:]
        else:
            self.buffer.pop(0)

        return byte

    def ungetc(self, char):
        '''Put the single byte char back into the buffer.

        char can be a multibyte string but things can get messed up if char
        contains any whitespace character.'''

        if not char:
            return

        if ' ' in char or '\t' in char or '\n' in char:
            raise CInException(char + 'not ungetable.')

        if len(self.buffer):
            self.buffer[0] = char + self.buffer[0]
        else:
            self.buffer.append(char)

    def getword(self):
        '''Return a single word from the input stream.'''

        self.fill_buffer()

        word = self.buffer[0]
        self.buffer.pop(0)

        return word

    def getint(self):
        '''Return an integer from the input stream.'''

        word = self.getword()

        num = ''
        for char in word:
            if not char.isdigit():
                break
            word = word[1:]
            num += char

        if num:
            self.ungetc(word)
            return int(num)
        else:
            raise CInException('Integer expected, got ' + word)

    def getfloat(self):
        '''Return a float from the input stream.'''

        pre_dot_num = str(self.getint())
        dot = self.getc()
        if dot != '.':
            self.ungetc(dot)
            return float(pre_dot_num)
        post_dot_num = str(self.getint())

        return float(pre_dot_num + dot + post_dot_num)

    def fill_buffer(self):
        '''Fill the buffer if empty.'''

        if not self.buffer:
            self.buffer = input().split()

    def empty_buffer(self):
        '''Fill before you empty!!!'''

        copy = self.buffer[:]
        self.buffer = []
        return copy

class CInException(Exception):
    '''Exception raised when something goes wrong.'''

    def __init__(self, err):
        Exception.__init__(self, err)


cinput = CIn()

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
        self.buffer = ''

    def getc(self):
        '''Read and return a single non-whitespace byte.'''

        self.fill_buffer()

        byte = self.buffer[0]
        self.buffer = self.buffer[1:]

        return byte

    def ungetc(self, chars):
        '''Put the single byte char back into the buffer.

        char can be a multibyte string but things can get messed up if char
        contains any whitespace character.'''

        if len(self.buffer):
            self.buffer = chars + self.buffer

    def getword(self):
        '''Return a single word from the input stream.'''

        self.fill_buffer()

        word = self.buffer.split()[0]
        self.buffer = self.buffer[len(word):].lstrip()

        return word

    def getint(self):
        '''Return an integer from the input stream.'''

        # skip whitespace
        char = ' '
        while char in {' ', '\t', '\n'}:
            char = self.getc()

        sign = char
        if sign not in {'-', '+'}:
            self.ungetc(sign)
            sign = ''

        digit = self.getc()
        if ord(digit) not in range(ord('0'), ord('9') + 1):
            raise CInException('Integer expected, got ' + digit)

        num = ''
        while digit.isdigit() and digit not in {' ', '\t', '\n'}:
            num += digit
            digit = self.getc()
        self.ungetc(digit)

        return int(num)

    def getfloat(self):
        '''Return a float from the input stream.'''

        pre_dot_num = str(self.getint())

        dot = ''
        post_dot_num = ''
        if self.peek() == '.':
            dot = self.getc()

            post_dot_digit = self.getc()
            if ord(post_dot_digit) not in range(ord('0'), ord('9') + 1):
                raise CInException('Integer expected, got ' + post_dot_digit)

            while post_dot_digit.isdigit() and post_dot_digit not in {' ', '\t', '\n'}:
                post_dot_num += post_dot_digit
                post_dot_digit = self.getc()
            self.ungetc(post_dot_digit)

        return float(pre_dot_num + dot + post_dot_num)

    def fill_buffer(self):
        '''Fill the buffer if empty.'''

        if not self.buffer:
            self.buffer = input() + '\n'

    def empty_buffer(self):
        '''Fill before you empty!!!'''

        copy = self.buffer
        self.buffer = ''
        return copy

    def peek(self):
        '''Return the next character in the buffer or None.'''

        return None if len(self.buffer) == 0 else self.buffer[0]

    def skip_whitespace(self):
        '''Remove whitespace from the start of the buffer.'''

        self.fill_buffer()
        self.buffer = self.buffer.lstrip()

class CInException(Exception):
    '''Exception raised when something goes wrong.'''

    def __init__(self, err):
        Exception.__init__(self, err)


cinput = CIn()


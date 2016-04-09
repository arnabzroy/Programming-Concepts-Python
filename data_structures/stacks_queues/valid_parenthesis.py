'''
If the code in S uses brackets correctly, output “Success” (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched
closing brackets, output the 1-based index of the first unmatched opening bracket.

# Strings which are paren, brackets and braces matched i.e. PBB matched
# "(){}[]"

# Answer:-
# Stack is best suited for parsing and matching operations
# "([{" => Left characters
# "]})" => Right characters
# Push if matching left characters
# Pop if matching right characters
# After Pop compare if left and right character matches

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3

import sys


class Bracket:

    def __init__(self, bracket_type='', position=0):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


__name__ = '__main__'
if __name__ == '__main__':

    # text = sys.stdin.read()

    text = '{'
    bkt = Bracket()
    ret = 0
    opening_brackets_stack = []
    for (i, next) in enumerate(text):
        if next == '(' or next == '[' or next == '{':

            # Process opening bracket, write your code here

            opening_brackets_stack.append(next)
            bkt.bracket_type = next

        if next == ')' or next == ']' or next == '}':

            # Process closing bracket, write your code here

            if len(opening_brackets_stack) == 0:
                ret = -1
                break
            bkt.bracket_type = opening_brackets_stack.pop()

            # print(next, bkt.bracket_type)

            if not bkt.Match(next):
                ret = -1
                break
    if ret == 0 and len(opening_brackets_stack) == 0:
        print 'Success'
    else:
        print i + 1

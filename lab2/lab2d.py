#!/usr/bin/env python3
'''
Name: Alyx Millan Andres
Course: Ops445NCC
'''
import sys

if len(sys.argv) != 3:
    print('usage: ' +  sys.argv[0] + ' name age')
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]
print('Hi ' + name + ', you are ' + str(age) + ' years old.')


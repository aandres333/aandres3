#!/usr/bin/env python3
#Author: Alyx Millan Andres
#Author ID: 106879224
#Date Created: 2024/05/29
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3
while timer != 0:
    print(timer)
    timer = timer - 1
print("blast off!")

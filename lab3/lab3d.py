#!/usr/bin/env python3
#Author ID: 106879224

import subprocess
import os

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    space = output[0].decode('utf-8').strip()
    return space
print(free_space())

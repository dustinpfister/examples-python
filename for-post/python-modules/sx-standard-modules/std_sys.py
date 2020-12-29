#!/usr/bin/python3
import sys

name="No Name"
if(len(sys.argv) >= 2):
    name=sys.argv[1]

print('Hello ' +name)
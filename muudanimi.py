#!/usr/bin/python

import os, sys

# Open a file
path = os.path.dirname(os.path.abspath(__file__))
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
    newfile = file.replace('(', '')
    newfile = newfile.replace(')', '')
    newfile = newfile.replace(' ', '')
    os.rename(file, newfile) 
    print (newfile)
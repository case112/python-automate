#!/usr/bin/python

#Removes all '(' and ')' and ' ' from file names in the same directory where the program is executed

import os, sys

print('')
print('Checking for files...')
print('---------------')

path = os.path.dirname(os.path.abspath(__file__))
dirs = os.listdir( path )
counter = 0


for file in dirs:
    newfile = file.replace('(', '')
    newfile = newfile.replace(')', '')
    newfile = newfile.replace(' ', '')
    os.rename(file, newfile)
    if file != newfile: 
        print ('+ ', file, ' ---> ', newfile)
        counter +=1

print('---------------')
print(counter, ' files changed.')
print('---------------')
input("Press enter to close program")
print('')
#!/usr/bin/python

from one import *;

def functionTwo():
    print ( 'functionTwo invoked ...' )
    print ( __name__ )

if __name__ == "__main__": 
   functionOne()
   functionTwo()

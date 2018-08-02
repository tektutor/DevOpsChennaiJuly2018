#!/usr/bin/python

class MyClass:

   def __init__(self):
       print ( "MyClass constructor" )
       self.x = 0
       self.y = 0

   def setValues(self, x, y ):
       self.x  = x
       self.y  = y

   def printValues(self):
       print ( "The value of x is ", self.x )
       print ( "The value of y is ", self.y )

def main():
    obj = MyClass()

    print ("Before setting values ...")
    obj.printValues()

    obj.setValues ( 100, 200 )

    print ("After setting values ...")
    obj.printValues()

main()

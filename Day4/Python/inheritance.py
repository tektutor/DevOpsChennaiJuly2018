#!/usr/bin/python
class Parent:
    def __init__(self):
        print ( 'Parent constructor' )
        self.x = 0
        self.y = 0

    def setValues(self, a, b ):
        self.x = a
        self.y = b

    def printValues(self):
        print ( 'The value of x is ', self.x )
        print ( 'The value of y is ', self.y )

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print ( 'Child constructor' )
        self.z = 0

    def setValues(self, a, b, c):
	Parent.setValues (self, a, b )
        self.z = c

    def printValues(self):
	Parent.printValues ( self )
        print ( 'The value of z is ', self.z )

def main():
    obj = Child()
    print ('Before setting values ...')
    obj.printValues()
    obj.setValues( 10, 20, 30 )
    print ('After setting values ...')
    obj.printValues()
    
main()

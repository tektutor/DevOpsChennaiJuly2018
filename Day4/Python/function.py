#!/usr/bin/python

def sayHello(msg): 
  print ( type ( msg ) )
  print ( msg )

'''
if __name__ == "__main__":
   print ( __name__ )
   sayHello( 'Hello Python!' )
   sayHello ( 1 )
   sayHello ( 1.0 )
'''

def main():
  print ( __name__ )
  sayHello( 'Hello Python!' )
  sayHello ( 1 )
  sayHello ( 1.0 )

main()

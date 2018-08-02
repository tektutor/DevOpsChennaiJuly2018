from ansible.module_utils.basic import *; 

class Add:
   def add ( self, x, y ):
       return x + y

def main():
   module = AnsibleModule(
	argument_spec= dict (
		firstInput = dict ( required=True, type='int' ),
		secondInput = dict ( required=True, type='int' )
	)
   )

   firstNumber  = module.params['firstInput']
   secondNumber = module.params['secondInput']

   addObj = Add()

   result = { "Result": str(addObj.add ( firstNumber, secondNumber )) }

   #module.exit_json ( changed=False, meta=result )
   module.fail_json ( "Fatal error" )


main()

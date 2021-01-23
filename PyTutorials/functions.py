
'''
Functions are blocks of code that may be executed one or more times while running some code.
they usually consist of an identifier/name ( like in a variable ), arguments/parameters and a function body.

They can also contain a return statement, but we'll get back to that a lil later.

Syntax for declaring a function is:


def FUNCTION_NAME ( ... arguments/parameters ... ):
    ...
    function_body
    ...

'''
# NOTE: Functions, in general, are useful for the purpose of avoiding repitition of code that needs to be executed
# multiple times.

'''
To execute what's in a function, we "call" the function (say, someFunc) like so:
someFunc()


Now, about the return statements. If you want to have a function do something and output a value (or anything), you'd have
to use a "return" statement.

Here's some examples to help you understand:
'''

# here's an example function:

#       /----------------------------------------| Function identifier/name
#       v
def add_two_numbers( a, b ):
#                     ^--------------------------| Arguments
    return a + b
#       ^----------------------------------------| return statement. ( "returns" the sum of numbers "a"
#                                                | and "b" passed in as arguments )

# calling the function:
var = add_two_numbers( 10, 20 )
# ^                     ^------------------------| Numbers passed will be assigned to "a" and "b" respectively
# |                                              | when the code inside the function body.
# |
# |----------------------------------------------| just a variable to store the value that's been returned

print("10 + 20 = ", var) # <-----------------------------------| printing the variable to check if the function call worked.

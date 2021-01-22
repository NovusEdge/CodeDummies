# variables are simply pieces of text the language can recognise and store value(s) in...

# * Note: The word "Syntax" refers to the "Grammar" of the programming language.

# syntax for declaring variables:

#? identifier = value
# example:




anInteger = 100 #* <------| The value assigned is just called "value"
#* ^
#* \ ---------| the "name" of the variable is called the "identifier"

print( anInteger ) #* <------| print is a "function" (we'll get to those later)
#*        ^
#*        \----------| The identifier "points" to it's value and thus it is 100 that's
#*                   | printed and not something else

#-------------------------------------------------------------------------------------------------------------------

someFloat = 1023.123
someString = "This is a String :)"

someList = [ 1, 2, 3, 4, 5, 6 ]
otherList = [ "string", 1, 123.123 ]

tuples = ( 1, 2, 3, 4, 5, 6 )

someDict = { "key1" : "value1", "amt": 10 }

#-------------------------------------------------------------------------------------------------------------------

Principal = int(input("enter the principal value:"))
Rate = int(input("enter the rate:"))
Time = 18 # time in years
Simple_int = Principal * Rate * Time/100
Amount = Principal + Simple_int

print("Simple_int = ", Simple_int)
print("Amount = ", Amount)


val = int(input("Enter some value: "))

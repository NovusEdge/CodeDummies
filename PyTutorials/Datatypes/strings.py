
# Strings are collections/sets of characters.
# A string in python can be declared in the following ways:

s = 'This is a string'
print(s)

s = "This is also a string :)"
print(s)

s = '''
This is a
multiline string.
'''
print(s)

s = """
This is also a
multiline string.
"""
print(s)


r'''

There's several "escape sequences" that are basically special characters that represent
different non-printable characters, which, serve several purposes:

Backslash notation  || 	Hexadecimal character  ||   	Description
--------------------||-------------------------||------------------
        \a 	    ||          0x07           ||    Bell or alert
        \b          ||          0x08   	       ||      Backspace
        \cx   	    ||                         ||      Control-x
        \C-x        ||                         ||  	   Control-x
        \e 	    ||          0x1b           ||       Escape
        \f          ||     	    0x0c       ||      Formfeed
        \M-\C-x     ||                         ||	 Meta-Control-x
        \n 	    ||          0x0a           ||       Newline
        \nnn        ||                         ||	 Octal notation, where n is in the range 0.7
        \r          ||    	    0x0d       ||    Carriage return
        \s          ||          0x20           ||        Space
        \t          ||     	    0x09       ||         Tab
        \v          ||          0x0b           ||     Vertical tab
        \x          ||                         ||  	   Character x
        \xnn        ||                         || 	 Hexadecimal notation, where n is in the range 0.9, a.f, or A.F
'''

para_str = """ This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up. """

print(para_str + "\n\n")

# Strings can also be thought of as lists of characters, so a character at the nth position will lie on the (n-1)th index.

'''                 _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _
    somestring = " |T| |h| |i| |s| | | |i| |s| | | |a| | | |s| |t| |r| |i| |n| |g|" = "This is a string"
                    ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^   ^
                    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15

    NOTE: indexing starts from 0
'''

# To access a character at a particular index, we use the bracket notation:

print("\n\nThis is a string"[10]) # should print "s"

var = "This is a string"
print(var[11]) # should print "t"

# A substring is basically a part of the string, i.e. a small section of the string.
# We use something known as "string slicing" to obtain a substring from a string.

# to slice strings in python, we use the bracket operator as well, but we define the bounds for slicing:
start = 3
end = 9

print( "This is a string"[ start : end ] )

# or alternatively
substr = "This is a string"[ start : end ]
print(substr)

# if either of the bounds are not defined/specified, then:
print( "This is a string"[ : end ] )
print( "This is a string"[ start: ] )

print( "This is a string"[ : ] ) # this prints the entire string

'''
Python also provides a huge array of string "methods"(functions) that allow us to do cool stuff with strings
A list of em can be found here :  https://www.tutorialspoint.com/python-string-methods

Go check em out!
'''

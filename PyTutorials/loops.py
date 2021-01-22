# Loops are for execution of operations over an iterable (or executing em a number of times...)

# There's 2 types of loops in python....
# for and while

'''
Syntax for the 'while' loop:

while <condition>:
    <code block>

else: # <--------------------------| The else block is optional, and we usually omit it.
    <do_somethin>                   The code under a while-else block will run after the
                                    main (while) loop is terminated.
'''

'''
                                                                    /---| By dummy variable we mean that it'll be discarded
Syntax for the 'for' loop:                                          |   | once the loop is terminated.
    /-------------------------------|                               v
    v                               |-----------| "iter" is just a dummy variable that the for loop will use
for iter in sequence:                           | as a placeholder for iterating over "sequence"
    statements(iter)                            | "sequence" can be either a list, a string, a dictionary or even a tuple
                                                | [So basically anything that is a collection of smaller stuff...]

else: <-----------------------------------------| Similar to the while loop, one can use the else block after the for loop
    <statements>                                | too. The code will be executed if the "iter in sequence" statement/condition
                                                | turns out to be false...
'''

# Some examples:

sequence = [1, 2, 3, 4, 10, 11, 12, 13]
someList = [1, "hello", ":)", "this can really be anythin", 123]

print("\n\n") # <----------| Just to make the output look a bit better :)
for i in sequence:
    print(i, end=", ") # <---------------------------------|
#                                                          |------------ Don't worry about the " end=', ' "s just now.
for any_arbitary_variable in someList: #                   |
    print(any_arbitary_variable, end=", ") # <-------------|



someString = "Hello World :)" # you may try and convert the string into a list of characters, go ahead and try it out! :)
                              # hint: there's something called "type-casting", loop it up!
# iterating over strings using the for loop
for character in someString:
    print(character, end=" ")


'''
We can alter the flow of the program while in a loop using some lil keywords, namely
-> break
-> continue
-> pass
(and also return but we'll get to that later...)

Here are some examples to help you understand what each of em do :)
'''

#-------------------------------------------break statement--------------------------------------------------

i = 0 # <------------| Just a variable -_-
while True: # <----------| This loop will run forever...
    if i == 10: # a conditional to check if i is equal to 10
    #   <some_code>
    #   ...
        break # <----\
#                    \-------- |the break statement will terminate the code and ignore any code after it...\
    i += 1 # <------------| increments 'i' by 1                                                            |
# <-------Basically putting the next line the intepreter will consider, over here--------------------------|

#------------------------------------------------------------------------------------------------------------

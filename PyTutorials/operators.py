'''
There's several operators in python, here's a list of em:

First there's the Arithmetic operators:

        Operator  |  Example
                  |
            +     |     1 + 2        list1 + list2
       (Addition) |   var1 + var2    string1 + string2 <---- this one's known as concatenation
                  |
                  |
            -     |     1 - 2        <no '-' operator for lists or strings>
     (Subtraction)|   var1 - var2
                  |
                  |
            *     |     1 * 2        string * n <--------- repeats the string n-number of times,  for example:
  (Multiplication)|   var1 * var2    "hello"*5 = "hellohellohellohellohello" (we can do the same with lists as well...)
                  |
                  |
            /     |     1 / 2       <no '/' operator for lists or strings>
       (Division) |   var1 / var2
                  |
                  |
            %     |     1 % 2       <no '%' operator for lists or strings>
       (Modulus)  |   var1 % var2
                  |
                  |
            //    |     1 // 2      <no '//' operator for lists or strings>
  (Floor-Division)|   var1 // var2
                  |
                  |
            **    |     1 ** 2      <no '**' operator for lists or strings>
  (Exponentiation)|   var1 ** var2

The (Integer-Division) Floor-Division operator truncates the decimal part of the result of division of numbers.

The Modulus operator gives us the remainder of 2 numbers when they're divided.
'''

# Examples of useage of Arithmetic operators:

print("Adding numbers:       1 + 2 = ", 1 + 2)
print("Adding(concatenating) strings: 'string1' + 'string2' = ", "string1" + "string2" )
print("Adding lists:         [1, 2, 3] + [4, 5, 6] = ", [1, 2, 3] + [4, 5, 6])

print("\nSubtracting numbers: 1 - 2 = ", 1 - 2)

print("\nMultipying numbers: 123 * 2784 = ", 123 * 2784)
print("Repeating strings: 'string1' * 5 ", "string1" * 5)
print(" '*' With lists: [0] * 10 = ", [0] * 10)

print("\nDividing:\nSimple-Division: 5/2 = ", 5/2, "\nFloor-Division: 5//2 = ", 5//2)
print("Modulus: 124%3 = ", 124%3)

print("\nExponentiation: 5**2 = ", 5**2)

'''
Next up, there's the Logical and Comparison operators:

        Operator  |  Example
                  |
            >     |     1 > 2        list1 > list2 <--------| In both lists and strings alike, the <(=) and >(=) operators
                  |   var1 > var2    string1 > string2 <----| will compare the elements/characters one-by-one.
                  |                                         | The first element to give false will cause the operation
            <     |     1 - 2        list1 < list2 <--------| to give the output/result as False. If no such occurence
                  |   var1 - var2    string1 < string2 <----| is there, the output/result is True.
                  |
            >=    |     1 >= 2       list1 >= list2 <-------| The main difference between the < and <=, and the > and >=
                  |   var1 >= var2   string1 >= string2 <---| operators is the strict inequality of < and >, i.e.
                  |                                         | 1 < 1 == False but 1 <= 1 == True.
            <=    |     1 <= 2       list1 <= list2 <-------|
                  |   var1 <= var2   string1 <= string2 <---|
                  |
            !=    |     1 != 2       list1 != list2 <-------| The != operator checks if the 2 variables/strings/lists/anything
                  |   var1 != var2   string1 != string2 <---| are equal and returns the opposite i.e. 1!=2 == True.
                  |
            ==    |     1 == 2       list1 == list2 <-------| The == ( equivalance ) operator helps check if something on the
                  |   var1 == var2   string1 == string2 <---| left side's equal to something on the right side.
                  |
            =     |   var = value   <-----------------------| This is the assignment operator, and is used to assign values to
                  |                                         | variables.
                  |
            and   | bool_1 and bool_2 ... <-----------------| Results in a 'True' boolean value if ALL of the operands are 'True'.
                  |
                  |
            or    | bool_1 or bool_2 ... <------------------| Results in a 'True' boolean value if any of the operands are 'True'.
                  |
                  |
            not   | not bool ... <--------------------------| Results in a 'True' value if 'bool' if 'False' and vise-versa.
'''

print("1 > 2 = ", 1 > 2)
print("1 < 2 = ", 1 < 2)

print("\n1 <= 2 = ", 1 <= 2)
print("1 >= 2 = ", 1 >= 2)
print("1 <= 1 = ", 1 <= 2)

print("\n1 != 2 = ", 1 != 2)
print("1 == 2 = ", 1 == 2)
print("1 == 1 = ", 1 == 1)

print("\nTrue and True = ", True and True)
print("True and False = ", True and False)
print("True and True and True ... = ", True and True and True)

print("\nTrue or True = ", True or True)
print("True or False = ", True or False)
print("True or False or True ... = ", True or False or True)

print("\nnot True = ", not True)
print("not False = ", not False)
print("\nTrue and not False = ", True and not False)


'''
Next up, there's the Bitwise operators:

        Operator        |  Example
                        |
            &           |   0110 & 0101 <---------------------| Each bit goes through an AND operation.
     (Bitwise - AND)    |    => 0100
                        |
                        |
            |           |   1010 | 0101 <---------------------| Each bit goes through an OR operation.
     (Bitwise - OR)     |    => 1111
                        |
                        |
            ~           |      ~1001 <------------------------| Each bit goes through an NOT operation.
     (Bitwise - NOT)    |    => 0110
                        |
                        |
            ^           |  1001 ^ 0101 <----------------------| Each bit goes through an XOR operation.
     (Bitwise - XOR)    |    => 1100
                        |
                        |
            >>          |  0101 >> n <------------------------| Performs a left shift on the number upto n bits.
   (Bitwise Left Shift) |
                        |
                        |
            <<          |  0101 << n <------------------------| Performs a right shift on the number upto n bits.
  (Bitwise Right Shift) |
'''

# There's some special operators as well!
# They are:
# 1) is <---------- True if the operands are identical (refer to the same object)
# 2) in <---------- True if value/variable is found in the sequence


# NOTE: Here's an operator precedence chart for reference: https://docs.python.org/3/reference/expressions.html#operator-precedence

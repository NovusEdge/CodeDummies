'''
There's several operators in python, here's a list of em:

First there's the Arithmetic operators:

        Operator  |  Example
                  |
            +     |     1 + 2        list1 + list2
       (Addition) |   var1 + var2    string1 + string2 <---- this one's known as concatenation
                  |
            -     |     1 - 2        <no '-' operator for lists or strings>
     (Subtraction)|   var1 - var2
                  |
            *     |     1 * 2        string * n <--------- repeats the string n-number of times,  for example:
  (Multiplication)|   var1 * var2    "hello"*5 = "hellohellohellohellohello" (we can do the same with lists as well...)
                  |
            /     |     1 / 2       <no '/' operator for lists or strings>
       (Division) |   var1 / var2
                  |
            %     |     1 % 2       <no '%' operator for lists or strings>
       (Modulus)  |   var1 % var2
                  |
            //    |     1 // 2      <no '//' operator for lists or strings>
  (Floor-Division)|   var1 // var2
                  |
            **    |     1 ** 2      <no '**' operator for lists or strings>
  (Exponentiation)|   var1 ** var2
                  |

The (Integer-Division) Floor-Division operator truncates the decimal part of the result of division of numbers.

The Modulus operator gives us the remainder of 2 numbers when they're divided
'''

# Examples of useage of Arithmetic operators:

print("Adding numbers:       1 + 2 = ", 1 + 2)
print("Adding(concatenating) strings: 'string1' + 'string2' = ", "string1" + "string2" )
print("Adding lists:         [1, 2, 3] + [4, 5, 6] = ", [1, 2, 3] + [4, 5, 6])

print("\n\nSubtracting numbers: 1 - 2 = ", 1 - 2)

print("\n\nMultipying numbers: 123 * 2784 = ", 123 * 2784)
print("Repeating strings: 'string1' * 5 ", "string1" * 5)
print(" '*' With lists: [0] * 10 = ", [0] * 10)

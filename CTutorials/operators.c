#include<stdio.h>

/*
There's several operators in python, here's a list of em:

First there's the Arithmetic operators:

        Operator  |  Example
                  |
            +     |     1 + 2
       (Addition) |   var1 + var2
                  |
                  |
            -     |     1 - 2
     (Subtraction)|   var1 - var2
                  |
                  |
            *     |     1 * 2
  (Multiplication)|   var1 * var2
                  |
                  |
            /     |     1 / 2
       (Division) |   var1 / var2
                  |
                  |
            %     |     1 % 2
       (Modulus)  |   var1 % var2
                  |
                  |
            ++    |     ++var <----------------------| ++var increments(by one) before a value is returned
      (Increment) |     var++ <----------------------| var++ increments(by one) after a value is returned
                  |
                  |
            --    |   --var  <-----------------------| --var decrements(by one) before a value is returned
      (Decrement) |   var--  <-----------------------| var-- decrements(by one) after a value is returned


The Modulus operator gives us the remainder of 2 numbers when they're divided.
*/



/*
Next up, there's the Logical and Comparison operators:

        Operator  |  Example
                  |
            >     |     1 > 2
                  |   var1 > var2
                  |
            <     |     1 - 2
                  |   var1 - var2
                  |
            >=    |     1 >= 2
                  |   var1 >= var2
                  |
            <=    |     1 <= 2
                  |   var1 <= var2
                  |
            !=    |     1 != 2
                  |   var1 != var2
                  |
            ==    |     1 == 2
                  |   var1 == var2
                  |
            &&    |   bool_1 && bool_2 <-----------------| performs a logical AND operation on the booleas.
                  |
                  |
            ||    |   bool_1 || bool_2 <-----------------| performs a logical OR operation on the booleans.
                  |
                  |
            !     |       !bool <------------------------| performs a logical NOT operation.
*/


/*
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
*/

int main() {
    // Examples of useage of Arithmetic operators:

    printf("Adding numbers:       1 + 2 = %d\n", 1 + 2);

    printf("\nSubtracting numbers: 1 - 2 = %d\n", 1 - 2);

    printf("\nMultipying numbers: 123 * 2784 = %d\n", 123 * 2784);

    printf("\nModulus: 124%%3 = %d\n", 124%3);

    int var = 10; // just a variable to for illustrating increment/decrement.
    printf("\nvar++: %d\n", var++);
    var = 10; // resetting the value of "var"
    printf("++var: %d\n", ++var);
    var = 10; // resetting the value of "var"

    printf("\nvar--: %d\n", var--);
    var = 10; // resetting the value of "var"
    printf("--var: %d\n", --var);
    var = 10; // resetting the value of "var"


    printf("\n1 > 2 = %d\n", 1 > 2);
    printf("1 < 2 = %d\n", 1 < 2);

    printf("\n1 <= 2 = %d\n", 1 <= 2);
    printf("1 >= 2 = %d\n", 1 >= 2);
    printf("1 <= 1 = %d\n", 1 <= 2);

    printf("\n1 != 2 = %d\n", 1 != 2);
    printf("1 == 2 = %d\n", 1 == 2);
    printf("1 == 1 = %d\n", 1 == 1);

    printf("\nTrue(1) && True(1) = %d\n", 1 && 1);
    printf("True(1) && False = %d\n", 1 && 0);
    printf("True(1) && True(1) && True(1) ... = %d\n", 1 && 1 && 1);
    printf("True(1) && False(0) && True(1) ... = %d\n", 1 && 0 && 1);

    printf("\nTrue(1) || True(1) = %d\n", 1 || 1);
    printf("True(1) || False(0) = %d\n", 1 || 0);
    printf("True(1) || True(1) || True(1) ... = %d\n", 1 || 1 || 1);
    printf("True(1) || False(0) || True(1) ... = %d\n", 1 || 0 || 1);

    printf("\n !True(1) = %d\n", !1);
    printf("!False(0) = %d\n", !0);
    printf("True(1) && !0 = %d\n",1 && !0);

}
// NOTE: Here's an operator precedence chart for reference: https://docs.microsoft.com/en-us/cpp/c-language/precedence-and-order-of-evaluation?view=msvc-160#precedence-and-associativity-of-c-operators

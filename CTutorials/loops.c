#include<stdio.h>

int main() {

    /*
    There's 3 types of loops in C:
    -> while    loop
    -> do-while loop
    -> for      loop

    Here's the syntax and an example for each of them:
    */

    // while loop:
    /*
    Syntax:

    while( condition ) {
        ...
        code_statements
        ...
    }

    example:
    */

    int var = 0; // <-------| A dummy variable that will help make the condition for the loop.

//             /----------------------| This is a sample condition, checking if variable is less than 10.
//             v                      | if this condition is true, the loop will start and code inside will be executed.
    while ( var < 10 ) {

        printf("%d, ", var); // <-----| Simply printing the variable.

        var++; // <-------------------| This line uses the increment operator (++) to increment the value of "var" by 1
               //                     | every iteration of the loop. ( Try removing it and see what happens :P )
               //                     | ( NOTE: use ctrl+C to terminate the program )
    }


}

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

    /*
    do-while loop:

    Syntax:

    do {
        ...
        code_statements
        ...
    } while (condition);

    example:
    */
    printf("\n\n"); // just adding newlines for readability in the console output

    var = 0; // <---------------------| We'll just use the perviously declared dummy variable.
             //                       | reassigned the value 0 to the variable for reusing it.

    do {

        printf("%d, ", var);
        var++; // <------------------------| yet again, just incrementing "var" and printing it.

    } while( var < 10 );
//              ^________________________________| As we can see, the condition is tested for AFTER the loop body is executed.
//                                               | however, in the simple while-loop, the condition was checked for BEFORE
//                                               | the loop body was executed.

    printf("\n\n");

    /*
    for loop:

    Syntax:
    for ( dummy-var; condition; increment/decrement ) {
        ...
        code_statements
        ...
    }

    example:
    */
//                                              |------------------------------increment/decrement.
//                                  |-----------|-------------------| Condition.
//              |-------------------|-----------|---------| Dummy variable declaration.
//              v                   v           v
    for ( int dummy_var = 0; dummy_var < 10; dummy_var++) {

        printf("%d, ", dummy_var);

    }

    // Note that we dont really require an increment/decrement statement IN the loop-body, but it's just defined in the
    // loop declaration.
}

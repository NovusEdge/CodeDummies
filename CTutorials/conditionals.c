#include<stdio.h>

int main() {

    /*
    ==> Basic syntax for an if-else statement is:

             /-------------| If this condition then the code_statements inside will be executed.
            v
    if ( condition ) {
        ...
        code_statements <-------------------| action to be taken w.r.t condition.
        ...
    }
    else { <-----------------------| The else block will run if all above conditions fail/are not executed.
        ...                        | We can omit the else block if nothing is to be done in the case all conditions fail.
        code_statements
        ...
    }

    In order to test for several conditions, we use "else if" blocks.

    if ( condition_1 ) {
        ...
        code_statements
        ...
    } else if ( condition_2 ) {
        ...
        code_statements
        ...
    }
    ... ( many more else-ifs later )
    else{
        ...
        code_statements
        ...
    }

    Here are some examples to help you understand...
    */

    int condition_1 = 0; // <-------| Since C doesnt have a boolean datatype, basically,
    int condition_2 = 1; //         | any non-zero integer will act as a "Truthy", value
    int condition_3 = 0; //         | So we may treat 1 as "True" and 0 as "False"


    if ( condition_1 ) {

        printf("Condition_1 is True :)\n"); // <----------------| printed if condition_1 is True.
                                            //                  | If the condition is False then everything in the
    } else if ( condition_2 ) {             //                  | block is ignored and the program tests for the next block.

        printf("Condition_2 is True :)\n"); // <----------------| printed if condition_2 is True.

    } else if ( condition_3 ) {

        printf("Condition_3 is True :)\n"); // <----------------| printed if condition_3 is True.

    } else {

        printf("None of the conditions are True :(\n"); // <----| printed if none of the conditions are True.

    }

    // You should take note that, in simple if-else if-else if ... else statements, the "else" block should come after all of
    // the condition blocks.

    // It is also important to take note that once any of the conditions are fulfilled, and the corresponding code_statements
    // are executed. all other code blocks of the corresponding "main-if" block are ignored and code after the else-block
    // (if any) is executed.

    // Whenever such a statement is implemented, where there's the process of "decision-making", the code "branches out".

    // There's something really interesting called "branchless programming", once you are familiar with programming,
    // try giving it a shot :)
}

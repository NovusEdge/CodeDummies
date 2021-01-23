#include<stdio.h>

/*
Functions are blocks of code that may be executed one or more times while running some code.
they usually consist of an identifier ( like in a variable ), arguments/parameters, a return-type and a function body.

Syntax for declaring a function is:

return_type FUNCTION_IDENTIFIER ( ... parameters ... ) {

    ...
    function_body
    ...

}

NOTE: Functions, in general, are useful for the purpose of avoiding repitition of code that needs to be executed
multiple times.

You may have noticed that we usually begin a c program using something like:

int main() {
    ...stuff...
}

which is, in fact, a function!
The compiler runs the code written in the main function when the code's executed.

Calling a function refers to when you have the program "run" the function i.e. whatever is in the function body.

To call a function (say, someFunction), we use:
someFunction()

Here's some examples to help you understand:
*/

//
//      /---------------------------------| The identifier is "add_two_numbers"
//      v
  int add_two_numbers(int a, int b) {
// ^                    ^-----^-----------| "a" and "b" are the arguments/parameters, you can use em in the function
// |                                      | and they are "passed into the function" when you call it in the main-function.
// |
// |--------------------------------------| Function's return type is "int"
    return a + b;
//      ^
//      |---------------------------------| "return" is a keyword. When you return something from a function,
//                                        | you're basically making it so that you can access the return-value
//                                        | whenever you call the function.
//                                        | When we return something from a function, the function is terminated
//                                        | after returning and any code after it will not be executed.

}

int main() {

//       |-----------------------------------------------| The value returned by "add_two_numbers" will be stored into "result"
//       v
    int result = add_two_numbers( 10, 20 ); // <---------| Here, "add_two_numbers" takes in 2 numbers, 10 and 20
    printf("10 + 20 = %d", result); //                   | which will be assigned to "a" and "b" respectively.

}

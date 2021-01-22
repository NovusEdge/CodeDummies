#include <stdio.h>


int main() {

    // Basic syntax for declaring a variable is:
    // type identifier;
    // OR
    // type identifier = value;  [don't forget the semicolon :)]
//  |-----------------------\
//  v                       |------------ Type of the variable
    int anInteger = 10; // <-------------------------------------- Value
        // ^
        // |---------------- Identifier

    int var; // <---------- garbage value stored in this variable...
    printf("Garbage value in var = %d\n", var);

    int True =  1;
    int False = 0;

    printf("%d && %d = %d\n", 1, 0, 1 && 0);

}

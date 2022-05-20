#include<stdio.h>

/*
 * Author: 	Aliasgar Khimani
 * Date: 	20 May 2022
 * Subject:	How to find the largest number in an array? 
 * */

// Function signature:
int max(int[], int);

int main() {
	// Test cases:
	//
	// Ayyay with all positives
	int array1[] = {1, 4, 7, 3, 7, 7, 2, 12, 346, 123, 5};
	int	max_array1 = max(array1, sizeof(array1)/sizeof(int));

	// Array with negative stuff
	int array2[] = {-1, -5, 0, -223, 1, 342, 0};
	int	max_array2 = max(array2, sizeof(array2)/sizeof(int));


	// Empty array
	int array3[] = {  };
	int	max_array3 = max(array3, sizeof(array3)/sizeof(int));

	printf("Max of array1 = %d\n", max_array1);
	printf("Max of array2 = %d\n", max_array2);
	printf("Max of array3 = %d\n", max_array3);

	return 0;
}

int max(int array[], int length) {
	// This is not necessary but it's good to have a few test-cases and checks
	// before you try and find the maximum value in an array
	if (length == 0) {
	// checking if the array is empty.
	// Since we're just woking with an example, we'll return 0 as the default max
	// value, but in real code, this is quite a stupid thing to do.
		return 0;

	} else if (length == 1) {
		// If the array only has one element, why bother checking?
		// Just return the element and save the computer lots of work.
		return array[0];
	} 
	
	// Now, since we're done with the checks, let's get onto the algorithm
	// itself.
	//
	// First we maintain a variable to store the largest value we can find.
	// This is the variable that the function will return.
	int result = array[0]; 
	// let's just make this the first element of the array since we'll be checking
	// all of the elements one-by-one
	
	// you can use any loop, but I'm using the for loop for this example:
	for(int i = 0; i < length; i++) {
		// now, we'll compare each number of the array to the number we have
		// in result. If the number is greater than result, we'll change
		// the value of result to that number.
		if (array[i] > result) {
			result = array[i]; 
		}
	}

	return result;
}

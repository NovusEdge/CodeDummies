public class Variables {
	public static void main(String[] args) {

		/*
		 * Variables are just like those in math, i.e. they store values for later use.
		 *
		 * We can declare variables using the following syntax: 
		 * <data_type> variable_name = value;
		 */

		// Here's some examples to demonstrate declaration of variables:

		int someInt = 10; // 32-bit number.

		// if the variable isn't assigned a value at declaration, it will hold a garbage value(bullshit value)
		
		// |--------1-byte
		// v
		boolean bool = true; // holds false if nothing is assigned.
		byte bt = 65; // translates to character: "A" when printed
		
		long longInt = 123971928; // 64-bit number
		short shortInt = 123; // 16-bit number

		float f = 123.123; // 4-bytes
		double df = 123.23876188; // 8-bytes

		char someChar = 'a'; // 2-bytes

		//Each of these datatypes are discussed a bit more in depth under the "DataTypes" Directory
	}
}

/*
 *
 * Here's a list of types of data avaliable in java: --> Primitives:
 
 	* boolean
	* byte
	* char
 	* short
 	* int
	* long
 	* float
 	* double

Primitive data can be thought as the simplest type of data that variables hold.

Non-Primitive data types refer to objects and hence they are called reference types. Examples of non-primitive types include
	* Strings
	* Arrays
	* Classes
	* Interface
	* and much more!
 */

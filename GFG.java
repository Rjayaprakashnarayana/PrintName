// Java Program to check accessibility of
// instance variables by static method

import java.io.*;

class GFG {
	
	// instance variable
	public int k;

	// Constuctor to set value to instance variable
	public GFG(int k) { this.k = k; }
	
	// set method for instance variable
	public void setK() { this.k = k; }
	
	// get method for instance variable
	public int getK() { return k; }

	public static void main(String[] args)
	{

		// Calling class GFG where instance variable is
		// present
		GFG gfg = new GFG(10);

		// now we got instance of instance variable class
		// with help of this class we access instance
		// variable
		System.out.print("Value of k is: " + gfg.getK());
	}
}

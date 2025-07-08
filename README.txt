801420902
Rayyan Habeeb
==============================================

Description:
In this project we have 3 tasks and in task 1 we evaluate a polynomial using horner's rule. 
This evaluation gives us a complexity of O(n^2). So, we implement Fast Fourier transform to evaluate the polynomial in o(nlogn).
In our task 2B, we compute the inverse fast fourier transform from input.
In task 3, the multiPolynomial method (multiplication of polynomials) is defined as the product of Fast fourier transforms of two polynomials and then finding the IFFT of this product in order to convert the polynomial back from frequency domain to time domain.
In the frequency domain, the multiplication of two polynomials is reduced to a simple element-wise multiplication of their transformed coefficients. This is much faster than the naive approach of multiplying each term of one polynomial by each term of the other.
Normal polynomial multiplication generally uses a time of O(n^2) where as FFT multiplication method uses O(nlogn)

=============================================

Program Design
The program is designed to read polynomial coefficients from input files, perform the necessary transformations and operations, and write the results to output files. The main tasks are divided into separate functions for clarity and modularity.

=============================================

Compiler:
The program is written in Python and can be executed using Python 3.8. No additional compilation is necessary.

=============================================

Failiures while writing the code:

The program assumes inputs are correctly formatted, the input is divided into two parts, it always considers the first part as real and the second part as imaginary.

The output may not always give the correct signs for 0s.

=============================================

How to Run:
>Place your input files in the same directory as Project.py
>Run the program using the command: python Project.py
>Follow the prompts to input file names for each task

=============================================

Data Structure Design:
>The program uses lists to store polynomial coefficients and results
>complex numbers are used to handle both real and imaginary parts of the coefficients.
>The paddingTwo function ensures that input lists are padded to the nearest power of two, which is necessary for efficient FFT computation.

=============================================

Summary of functionality:

Importing complex math library for accurate values of Pi and exponential function. Therefore we use cmath.pi and cmath.exp to calculate the principle nth root. since python doesn't have a double data type, we use float to store values.

The methods ComplexInput and ComplexOutput 


Task 1: 
in hornersRule(inputFile):
> We process input by taking in each line from the input text. Each line represents the coefficient of x^0,x^1... till n lines (where n is the total number of lines) strip it of spaces, split it into two parts a real and imaginary convert all of it into float using map(). The data structure of polynomial representation is a list which stores the polynomial coefficients in complex type i.e it has a real part and imaginary part.
>W = cmath.exp((2j * cmath.pi / alen)) calculates the nth roots by of unity (by using e^(ix) = cosx +isinx) and stores in complex form
>Assigning yk as highest degree's coefficient.
>In the two for loops, we iterate first time for taking different W values i.e W1,W2,W3, initializing yk as highest each time as  and for each value we iterate the loop from coefficient of second highest degree to constant summing each term. 
>We output the real and imaginary values of the final yk frequency value till 3 decimal places.
>Since we have a outter loop running from alen (n) times and inner one for alen-1 (n-1) one, the time complexity can be taken as O(n^2) 

---------------------------------------------------

Task 2a and 2b:
>In this task we implement Fast Fourier transform. 
>For input, complexInput method is defined. It takes the input which checks the number of parts the input has and append the input in complex type. This operation takes O(n) time.
>For FFT we use paddingTwo(a) function to add 0's in the input such it is to nearest power of 2, this improves the accuracy as well as help in setting up recurrence function.

--------------
FFT():
>Implementing FFT as per the pseudocode provided, using list data structure for storing co efficients of the polynomial. 
>sign: Determines whether to compute the FFT (sign = 1) or the inverse FFT (sign = -1).
>if n==1, then it is the base case and the size of input list is 1. The function returns itself and stops the recursion
>if n == +1 it calculates principal nroots of unity for ffts and n == -1 it calculates n roots for inverse fft.
>divide the input into coefficients of even terms and coeff of odd terms
>calling the FFT to compute the even indexed coefficients recursively and the same for odd indexed coefficients
>initialize a list with n 0's
>in a loop that iterates half the times of n
>y[k] = yeven[k] + W * yodd[k]: Multiplying W wo odd so we can rotate the results of odd indexed elements
> y[k + n // 2] = yeven[k] - W * yodd[k]: combining the elements and subtracting W*Yodd to maintain symmetry and correctly compute positive and negative frequency components of input
> return Y
>FFT takes a time complexity of O(nlogn), it uses divide and conquer methodology
--------------

IFFT(a,n):
>The input is vector of (possibly complex) numbers
>It calls FFT with sign -1.
> result[i] = result[i] / n The mathematical definition of IFFT has a scaling factor of 1/n to ensure the transformation is actually inverse of the fft. Since the FFT scales ouput by n, the result of IFFT is normalized by n.

-------------

Task3: Multiplying polynomials:
>The naive method i.e comparing the degrees and multiplying their coefficients takes O(n^2).
>Multiplying the FFTS of the polynomial, then inversing it's product takes a lot lesser time i.e O(nlogn).
>in multiPolynomial(a,b) we give two polynomials as inputs.
>the size of padding is calculated according to the size of the highest polynomial. The number of 0's are the next powers of 2 of bigger polynomial.
>perform FFT on both polynomials.
>Cfft is the product of both polynomials in frequency domain. Multiplication is computationally more efficient.
>Then Find IFFT of Cfft to get the product.

----------
Task2a(), Task2b(), Task3() method take in input and process it according to functions that are going to be applied in that particular task.

=========================================================

Conclusion:

The program successfully reads polynomial coefficients from input files and writes the results to output files.
The FFT and IFFT implementations are efficient and handle complex numbers correctly.
Polynomial multiplication is performed efficiently using the FFT and IFFT.


=========================================================

References: 
>The Remarkable Story Behind The Most Important Algorithm Of All Time: https://www.youtube.com/watch?v=nmgFG7PUHfo 
>CLRS4e, Chapter 30: Polynomials and the FFT.
>The Fast Fourier Transform (FFT): Most Ingenious Algorithm Ever? Reducible: https://www.youtube.com/watch?v=h7apO7q16V0
>cmath documentation: https://cplusplus.com/reference/cmath/





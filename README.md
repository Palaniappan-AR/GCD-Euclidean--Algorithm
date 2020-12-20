# GCD-Euclidean--Algorithm
Python program to find gcd of two numbers
Euclidean algorithms (Basic and Extended):

GCD of two numbers is the largest number that divides both of them. A simple way to find GCD is to factorize both numbers and multiply common factors.

EX:

36=2*2*3*3
60=2*2*3*5

GCD=Multiplication of common factors
   =2*2*3
   =12

Basic Euclidean Algorithm for GCD:

The algorithm is based on below facts.

->If we subtract smaller number from larger (we reduce larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.

->Now instead of subtraction, if we divide smaller number, the algorithm stops when we find remainder 0.

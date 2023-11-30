'''
BOJ 24171 - Complex Number (https://www.acmicpc.net/problem/24171)

Given two complex numbers A and B, print A + B, A - B, A * B, A / B.
'''

import sys
from math import gcd, lcm
from fractions import Fraction


# 3. ADDITION

def addition(A, B):
    
    real_no_root = A.real_no_root + B.real_no_root
    real_root = A.real_root + B.real_root
    
    a0 = lcm(real_no_root.denominator, real_root.denominator)
    b0 = real_no_root.numerator * (a0 // real_no_root.denominator)
    c0 = real_root.numerator * (a0 // real_root.denominator)
    d0 = A.d0
    if c0 == 0:
        d0 = 0
    
    imaginary_no_root = A.imaginary_no_root + B.imaginary_no_root
    imaginary_root = A.imaginary_root + B.imaginary_root
    
    a1 = lcm(imaginary_no_root.denominator, imaginary_root.denominator)
    b1 = imaginary_no_root.numerator * (a1 // imaginary_no_root.denominator)
    c1 = imaginary_root.numerator * (a1 // imaginary_root.denominator)
    d1 = B.d0
    if c1 == 0:
        d1 = 0
    
    return Complex([a0, b0, c0, d0, a1, b1, c1, d1])


# 5. MULTIPLICATION

def multiplication(A, B):
    
    d = A.d0
    
    real_no_root = A.real_no_root * B.real_no_root + A.real_root * B.real_root * d - A.imaginary_no_root * B.imaginary_no_root - A.imaginary_root * B.imaginary_root * d
    real_root = A.real_no_root * B.real_root + A.real_root * B.real_no_root - A.imaginary_no_root * B.imaginary_root - A.imaginary_root * B.imaginary_no_root
    
    a0 = lcm(real_no_root.denominator, real_root.denominator)
    b0 = real_no_root.numerator * (a0 // real_no_root.denominator)
    c0 = real_root.numerator * (a0 // real_root.denominator)
    d0 = A.d0
    if c0 == 0:
        d0 = 0
    
    imaginary_no_root = A.real_no_root * B.imaginary_no_root + A.real_root * B.imaginary_root * d + A.imaginary_no_root * B.real_no_root + A.imaginary_root * B.real_root * d
    imaginary_root = A.real_no_root * B.imaginary_root + A.real_root * B.imaginary_no_root + A.imaginary_no_root * B.real_root + A.imaginary_root * B.real_no_root
    
    a1 = lcm(imaginary_no_root.denominator, imaginary_root.denominator)
    b1 = imaginary_no_root.numerator * (a1 // imaginary_no_root.denominator)
    c1 = imaginary_root.numerator * (a1 // imaginary_root.denominator)
    d1 = B.d0
    if c1 == 0:
        d1 = 0
        
    return Complex([a0, b0, c0, d0, a1, b1, c1, d1])


# 6. TO GET THE INVERSE OF B FOR DIVISION

def inverse(B):
    
    d = B.d0
    
    # To make the denominator real : P + Q * sqrt(d)
    P = B.real_no_root ** 2 + B.real_root ** 2 * d + B.imaginary_no_root ** 2 + B.imaginary_root ** 2 * d
    Q = 2 * (B.real_no_root * B.real_root + B.imaginary_no_root * B.imaginary_root)
    
    denominator = P ** 2 - Q ** 2 * d
    
    real_no_root = Fraction(B.real_no_root * P - B.real_root * Q * d, denominator)
    real_root = Fraction(B.real_root * P - B.real_no_root * Q, denominator)
    
    a0 = lcm(real_no_root.denominator, real_root.denominator)
    b0 = real_no_root.numerator * (a0 // real_no_root.denominator)
    c0 = real_root.numerator * (a0 // real_root.denominator)
    
    imaginary_no_root = Fraction(B.imaginary_root * Q * d - B.imaginary_no_root * P, denominator)
    imaginary_root = Fraction(B.imaginary_no_root * Q - B.imaginary_root * P, denominator)
    
    a1 = lcm(imaginary_no_root.denominator, imaginary_root.denominator)
    b1 = imaginary_no_root.numerator * (a1 // imaginary_no_root.denominator)
    c1 = imaginary_root.numerator * (a1 // imaginary_root.denominator)
    
    return Complex([a0, b0, c0, d, a1, b1, c1, d])


# 1. TO CONSTRUCT CLASS FOR COMPLEX NUMBERS FOR EASY CALCULATION

class Complex:
    
    def __init__(self, arr):
        
        self.a0, self.b0, self.c0, self.d0 = arr[0], arr[1], arr[2], arr[3]
        self.a1, self.b1, self.c1, self.d1 = arr[4], arr[5], arr[6], arr[7]
        
        self.real_no_root = Fraction(self.b0, self.a0)
        self.real_root = Fraction(self.c0, self.a0)
        self.imaginary_no_root = Fraction(self.b1, self.a1)
        self.imaginary_root = Fraction(self.c1, self.a1)

    def __repr__(self):
        
        return str(self.a0) + " " + str(self.b0) + " " + str(self.c0) + " " + str(self.d0) + " " + str(self.a1) + " " + str(self.b1) + " " + str(self.c1) + " " + str(self.d1)


# 2. TO GET INPUT

A = Complex(list(map(int, sys.stdin.readline().split())))
B = Complex(list(map(int, sys.stdin.readline().split())))


# 4. TO NEGATIZE B FOR SUBTRACTION

negative_B = Complex([B.a0, -B.b0, -B.c0, B.d0, B.a1, -B.b1, -B.c1, B.d1])


# 7. TO SOLVE THE PROBLEM

print(addition(A, B))
print(addition(A, negative_B))
print(multiplication(A, B))
print(multiplication(A, inverse(B)))
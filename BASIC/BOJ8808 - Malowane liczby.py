'''
BOJ 8808 - Malowane liczby (https://www.acmicpc.net/problem/8808)

All positive rational numbers are colored either red or blue by the following conditions:
(1) Numbers differing by 1 are painted with different colors.
(2) Reciprocal numbers are painted with the same color.
(3) 1 is painted in red.

If a positive rational number is given, print what color the number would be: czerwony if red, niebieski otherwise.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    num = list(sys.stdin.readline().strip().split())
    
    numerator = int(num[0])
    denominator = int(num[2])
    
    # 2. TO SOLVE THE PROBLEM
    # The variable change stores how many times the color has changed to reach 1. 
    
    change = 0
    
    # Let's change the number to an integer.

    while numerator % denominator != 0:
        if numerator > denominator:
            change += numerator // denominator
            numerator %= denominator
        if numerator < denominator:
            numerator, denominator = denominator, numerator

    # Then, the problem gets way easier.
    
    change += (numerator // denominator) - 1
    
    if change % 2 == 0:
        print("czerwony")
    else:
        print("niebieski")
    
    
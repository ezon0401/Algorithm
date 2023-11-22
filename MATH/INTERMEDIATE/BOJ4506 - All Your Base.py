'''
BOJ 4506 - All Your Base (https://www.acmicpc.net/problem/4506)

The "base" is a number system where the N-th right-most digit can have values between 0 and N (1 <= N <= Z).
Given a "base" operation, determine whether it is valid or not.
If it is valid, calculate the result. 
'''

import sys


# 3. FUNCTIONS TO SOLVE THE PROBLEM

key = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# A function to check whether a number is valid

def check(num):
    
    if num[0] == "-":
        num = num[1:]
    
    ok = True
    if len(num) > 35:
        ok = False
    else:
        for index in range(1, len(num) + 1):
            if key.find(num[-index]) > index:
                ok = False
                break
    
    return ok

# A function to convert a base number into the decimal value

def convert_to_val(num):
    
    minus = 1
    if num[0] == "-":
        num = num[1:]
        minus = -1
        
    val = 0
    for index in range(1, len(num) + 1):
        val += key.find(num[-index]) * factorial[index]
    
    return val * minus
    
# A function to convert a decimal value into the base number

def convert_to_num(val):
    
    num = []
    if val < 0:
        num.append("-")
        val = abs(val)
        
    leading_zero = True
    for index in range(35, 0, -1):
        if leading_zero and val // factorial[index] == 0:
            continue
        else:
            num.append(key[val // factorial[index]])
            val %= factorial[index]
            leading_zero = False
    
    if len(num) == 0:
        return 0
    else:
        return "".join(num)


# 2. PRE-PROCESSING 
# Each digit in the "base" represents factorial values. 

factorial = [1, 1]
for num in range(2, 36):
    factorial.append(factorial[-1] * num)

max_val = convert_to_val("ZYXWVUTSRQPONMLKJIHGFEDCBA987654321")
min_val = -max_val


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    num1, op, num2 = sys.stdin.readline().strip().split()
    
    
    # 4. TO SOLVE THE PROBLEM
    
    if check(num1) and check(num2):
        if op == "+":
            val1 = convert_to_val(num1)
            val2 = convert_to_val(num2)
            if min_val <= val1 + val2 <= max_val:
                print(convert_to_num(val1 + val2))
            else:
                print("Invalid")
        else:
            val1 = convert_to_val(num1)
            val2 = convert_to_val(num2)
            if min_val <= val1 - val2 <= max_val:
                print(convert_to_num(val1 - val2))
            else:
                print("Invalid")
    else:
        print("Invalid")
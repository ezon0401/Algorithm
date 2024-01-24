'''
BOJ 1019 - Book Page (https://www.acmicpc.net/problem/1019)

Print how many times each digit appears from 1 to N.
'''

import sys


# 1. TO GET THE INPUT

page_num = list(sys.stdin.readline().strip())


# 2. TO SOLVE THE PROBLEM
# The basic idea is to calculate how many times each digit appears at each location.

digit_count = [0 for index in range(10)]

for index in range(len(page_num)):
    
    digit = int(page_num[index])
    
    if index == 0:
        
        for num in range(1, 10):
            if num < digit:
                digit_count[num] += pow(10, len(page_num) - index - 1)
            elif num == digit:
                if len(page_num) != 1:
                    digit_count[num] += int("".join(page_num[1:])) + 1
                else:
                    digit_count[num] += 1
            
    elif 0 < index < len(page_num) - 1:
        
        for num in range(10):
            digit_count[num] += int("".join(page_num[:index])) * pow(10, len(page_num) - index - 1)
            if num < digit:
                digit_count[num] += pow(10, len(page_num) - index - 1)
            elif num == digit:
                digit_count[num] += int("".join(page_num[index+1:])) + 1
        digit_count[0] -= pow(10, len(page_num) - index - 1)
    
    else:
        
        for num in range(10):
            digit_count[num] += int("".join(page_num[:index])) 
            if num <= digit:
                digit_count[num] += 1
        digit_count[0] -= 1
        
print(" ".join(map(str, digit_count)))
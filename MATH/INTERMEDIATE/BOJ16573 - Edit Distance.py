'''
BOJ 16573 - Edit Distance (https://www.acmicpc.net/problem/16573)

Given a binary string S, print any string T so that |S| = |T| and edit(S, T) > |S| / 2.
'''

import sys


# 1. A FUNCTION FOR CASES WHEN |S| IS ODD

def fill(string):
    
    zero_count = string.count("0")
    one_count = string.count("1")
    
    if zero_count < one_count:
        return "0" * len(string)
    else:
        return "1" * len(string)


# 2. TO SOLVE THE PROBLEM

string = sys.stdin.readline().strip()

ans = ""

if len(string) % 2 == 0:
    
    if string[0] == "0":
        ans += "1"
    else:
        ans += "0"
    string = string[1:]

ans += fill(string)
    
print(ans)
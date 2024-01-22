'''
ABC337B - Extended ABC (https://atcoder.jp/contests/abc337/tasks/abc337_b)

A string S is an Extended X string if all characters in S are X.
A string S` is an Extended ABC string if S` = Extended A string + Extended B string + Extended C string.
Determine if given string is Extended ABC string or not. 
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

string = sys.stdin.readline().strip()

result = ""
now = None
for char in string:
    if now == None or char != now:
        result += char
        now = char

correct = ["A", "B", "C", "AB", "AC", "BC", "ABC"]
if result in correct:
    print("Yes")
else:
    print("No")
'''
ABC332A - 202<s>3</s> (https://atcoder.jp/contests/abc335/tasks/abc335_a)

Change the last character of a string from 3 to 4. 
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

sentence = list(sys.stdin.readline().strip())
sentence[-1] = '4'
print("".join(sentence))
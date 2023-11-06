'''
BOJ 30458 - Palindrome Anagram (https://www.acmicpc.net/problem/30458)

There is a string S.
One can perform the following operation multiple times: Choose one from left N // 2 characters and one from right N // 2 characters, then swap them.
Is it possible to make S palindrome?
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
word = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

# To count how many times each character appears

alphabet_count = [0 for index in range(26)]

for index in range(length // 2):
    alphabet_count[ord(word[index]) - 97] += 1
    alphabet_count[ord(word[-index-1]) - 97] += 1
    
# To check each character appears even times
# It can be proved that each character can swap with any other characters.

possible = True

for alphabet in range(26):
    if alphabet_count[alphabet] % 2 != 0:
        possible = False
        break

if possible:
    print("Yes")
else:
    print("No")
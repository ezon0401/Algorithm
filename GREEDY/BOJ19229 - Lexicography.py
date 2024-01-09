'''
BOJ 19229 - Lexicography (https://www.acmicpc.net/problem/19229)

There are n X l letters.
Create n words of length l so that the k-th of them in the lexicographical order is lexicographically as small as possible.
'''


import sys
from collections import deque


# 2. A FUNCTION TO FILL THE TARGET WORD

def fill():
    
    start_index = target_index
    while start_index > 0 and len(ans[start_index-1]) == len(ans[target_index]) and ans[start_index-1][-1] == ans[target_index][-1]:
        start_index -= 1
    for index in range(start_index, target_index + 1):
        ans[index] += letters.popleft()


# 1. TO GET THE INPUT

word_count, word_length, target_index = map(int, sys.stdin.readline().split())
target_index -= 1
letters = list(sys.stdin.readline().strip())
letters.sort()
letters = deque(letters)


# 3. TO SOLVE THE PROBLEM

ans = ["" for word in range(word_count)]
for index in range(target_index + 1):
    ans[index] += letters.popleft()
for index in range(word_count-1, target_index, -1):
    ans[index] += letters.pop()

while len(ans[target_index]) < word_length:
    fill()

while len(letters) != 0:
    for index in range(word_count):
        if len(ans[index]) != word_length:
            ans[index] += letters.popleft()

for word in ans:
    print(word)
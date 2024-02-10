'''
BOJ 1497 - Guitar Concert (https://www.acmicpc.net/problem/1497)

There are N guitars. Scores each guitar can play are given.
Determine the minimum number of guitars needed to play the maximum number of scores.
'''

import sys
from itertools import combinations


# 1. TO GET THE INPUT

guitar_count, score_count = map(int, sys.stdin.readline().split())
arr = []

for guitar_input in range(guitar_count):
    guitar, possible_score = sys.stdin.readline().strip().split()
    arr.append(possible_score)


# 2. TO SOLVE THE PROBLEM

max_score = 0
ans = -1

for choice_count in range(1, guitar_count+1):
    for combination in combinations(arr, choice_count):
        
        check = ['N' for score in range(score_count)]
        
        for guitar in combination:
            for score in range(score_count):
                if guitar[score] == 'Y':
                    check[score] = 'Y'
        
        possible_score = check.count('Y')
        if max_score < possible_score:
            max_score = possible_score
            ans = choice_count

print(ans)
'''
BOJ 25904 - Hi, Cleopatra. The Best Potato Chip in the World (https://www.acmicpc.net/problem/25904)

'Hi, Cleopatra. The Best Potato Chip in the World' is a Korean drink game.
Everyone has to sing a note higher than the person before. 
Given the start node and the highest note each person can sing, determine who will drink.
'''

import sys


# 1. TO GET THE INPUT

player_count, start_note = map(int, sys.stdin.readline().split())
max_note = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

now_note = start_note
now_player = 0

while max_note[now_player] >= now_note:
    
    now_player = (now_player + 1) % player_count
    now_note += 1

print(now_player + 1)
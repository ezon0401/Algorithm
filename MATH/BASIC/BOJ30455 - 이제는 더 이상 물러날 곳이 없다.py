'''
BOJ 30455 - No more place to retreat (https://www.acmicpc.net/problem/30455)

Duck and Goose are fighting on a battlefield of length N. 
Duck starts at the leftmost cell, and Goose starts at the rightmost cell.
In their turn, they must move to an adjacent cell. If an opponent is in the cell, one can attack the opponent. 
The first one who attacks wins. The duck moves first.
Determine who will win the battle. 
'''

import sys


# 1. TO SOLVE THE PROBLEM
# A player in his turn wins when the distance between two players is 1.
# Each move is to decrease the distance by 1. 

field_size = int(sys.stdin.readline())

if field_size % 2 == 0:
    print("Duck")
else:
    print("Goose")
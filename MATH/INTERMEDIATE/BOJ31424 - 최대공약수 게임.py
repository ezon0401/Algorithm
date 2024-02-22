'''
BOJ 31424 - GCD Game (https://www.acmicpc.net/problem/31424)

There are N cards. A number X is written on a chalkboard.
Two layers do the following at each turn:

(1) Choose a card P from N cards. If a number Q is written on a chalkboard, gcd(P, Q) should not be 1.
(2) Write gcd(P, Q) on the board and erase Q.
(3) Remove the card P from the cards.

If there is no card to choose, the player loses.
Given two players play the best move, determine the winner. 
'''

import sys
from math import gcd


# 1. TO GET THE INPUT

card_count, start_num = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))


# 2. TO GET DIVISORS AND THEIR NUMBERS OF MULTIPLES
# Only divisors of start_num can be on the chalkboard.
# The number of multiples indicate how long the number on chalkboard can stay.

divisors = []
for divisor in range(1, int(start_num ** 0.5) + 1):
    if start_num % divisor == 0:
        divisors.append(divisor)
        if divisor != start_num // divisor:
            divisors.append(start_num // divisor)
divisors.sort()

divisor_count = len(divisors)

divisor_to_index = {}
for index in range(divisor_count):
    divisor_to_index[divisors[index]] = index

multiple_count = [0 for index in range(divisor_count)]
for index in range(len(divisors)):
    for card in cards:
        if card % divisors[index] == 0:
            multiple_count[index] += 1


# 3. DP

dp = [[0 for index in range(divisor_count)] for finished_turn in range(card_count + 1)]

# Player loses if he makes 1.

for finished_turn in range(1, card_count+1):
    
    player = finished_turn % 2 + 1
    opposite = 3 - player
    
    dp[finished_turn][0] = player

for index in range(1, divisor_count):
    
    num_on_board = divisors[index]
    
    for finished_turn in range(multiple_count[index], -1, -1):
        
        # Player loses if there is no card to choose or no way to win.
        
        player = finished_turn % 2 + 1
        opposition = 3 - player
        
        dp[finished_turn][index] = opposition
        
        if finished_turn != card_count:
        
            # Player wins if he can win the game by making a move.
            
            if finished_turn < multiple_count[index]:
                if dp[finished_turn+1][index] == player:
                    dp[finished_turn][index] = player
            
            for card in cards:
                if card % num_on_board != 0:
                    if dp[finished_turn+1][divisor_to_index[gcd(card, num_on_board)]] == player:
                        dp[finished_turn][index] = player


if dp[0][-1] == 1:
    print("First")
else:
    print("Second")
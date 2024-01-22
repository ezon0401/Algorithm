'''
BOJ 16565 - N-Poker (https://www.acmicpc.net/problem/16565)

A player chooses N cards among a trump card set.
Determine the number of cases of which there are four of a kind.
'''

import sys


# 2. A FUNCTION TO COUNT THE NUMBER OF COMBINATIONS

def combination(total, choice):
    return factorial[total] // (factorial[total-choice] * factorial[choice]) 

factorial = [1]
for num in range(1, 53):
    factorial.append(factorial[-1] * num)


# 1. TO GET THE INPUT

card_count = int(sys.stdin.readline())


# 3. TO SOLVE THE PROBLEM (Inclusion-Exclusion Principle)

max_four_card = card_count // 4

ans = 0
plus = True
for four_card in range(1, max_four_card + 1):
    count = combination(13, four_card) * combination(52 - 4 * four_card, card_count - 4 * four_card)
    if plus:
        ans += count
    else:
        ans -= count
    plus = not plus

print(ans % 10007)
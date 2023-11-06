'''
BOJ 30454 - Find a Zebra! (https://www.acmicpc.net/problem/30454)

Each binary string represents a zebra: 0 indicates white, and 1 indicates black.
The number of black stripes equals the number of continuous black parts.
How many stripes do zebras with the most stripes have? How many zebras have the most stripes?
'''

import sys


# 1. A FUNCTION TO COUNT THE NUMBER OF STRIPES OF ZEBRA

def count_stripe(zebra):
    
    count = 0
    before = "0"
    
    for index in range(zebra_length):
        if before == "0" and zebra[index] == "1":
            count += 1
        before = zebra[index]
    
    return count


# 2. TO SOLVE THE PROBLEM

zebra_count, zebra_length = map(int, sys.stdin.readline().split())

best = 0
count = 0

for zebra_input in range(zebra_count):
    zebra = sys.stdin.readline().strip()
    zebra_line = count_stripe(zebra)
    if zebra_line > best:
        best = zebra_line
        count = 1
    elif zebra_line == best:
        count += 1

print(best, count)
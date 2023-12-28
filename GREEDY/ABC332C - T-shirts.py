'''
ABC332C - T-shirts (https://atcoder.jp/contests/abc332/tasks/abc332_c)

For each day, Takahashi has no plan, a plan to go out for a meal, or a plan to attend a programming contest.
He will wear any shirt for a meal and only a logo T-shirt for a contest.
On days with no plans, he will not wear any T-shirts and wash all T-shirts worn.
Once he wears a T-shirt, he cannot wear it again until he washes it.

What is the minimum number of T-shirts he needs to buy given the schedule?
'''

import sys


# 1. TO GET THE INPUT

day_count, plain_count = map(int, sys.stdin.readline().split())
schedule = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

plain_available = plain_count
logo_available = 0

logo_bought = 0

for day in schedule:
    
    if day == "0":
        plain_available = plain_count
        logo_available = logo_bought
    
    elif day == "1":
        if plain_available:
            plain_available -= 1
        elif logo_available:
            logo_available -= 1
        else:
            logo_bought += 1
    
    else:
        if logo_available:
            logo_available -= 1
        else:
            logo_bought += 1
            
print(logo_bought)
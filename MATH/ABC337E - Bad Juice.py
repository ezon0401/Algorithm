'''
ABC337E - Bad Juice (https://atcoder.jp/contests/abc337/tasks/abc337_e)

Among N bottles of juice, a bottle is spoiled.
You can call friends and serve them some of the bottles to check the bottles.
Determine the minimum necessary number of friends.
Moreover, given the result of a check, print the number of the spoiled bottle.
'''

import sys

# 1. TO GET THE INPUT

juice_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# The key idea is that the minimum necessary number of friends equal to the length of the binary expression of (juice_count - 1).

friend_count = len(bin(juice_count - 1)[2:])
print(friend_count)
sys.stdout.flush()

drink = [[] for friend in range(friend_count)]
for juice in range(juice_count):
    key = bin(juice)[2:]
    key = "0" * (friend_count - len(key)) + key
    for friend in range(friend_count):
        if key[friend] == "1":
            drink[friend].append(str(juice + 1))

for friend in range(friend_count):
    print(len(drink[friend]), " ".join(drink[friend]))
    sys.stdout.flush()

result = sys.stdin.readline().strip()
print(int(result, 2) + 1)
sys.stdout.flush()
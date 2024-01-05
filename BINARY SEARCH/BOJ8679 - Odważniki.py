'''
BOJ 8679 - Weights (https://www.acmicpc.net/problem/8679)

There are N black weights, N grey weights, and N very light scales.
Bajtek recursively puts a black weight at one hand, and a scale at the other hand.
There will be an empty spot at the top scale. 
If Bajtek can balance any scale by putting a grey weight on the empty spot, Bajtek can replace the whole scale with a grey weight with equivalent mass if possible.
Determine the minimum number of weights Bajtek can leave. 
'''

import sys
from bisect import bisect_left


# 3. A BINARY SEARCH FUNCTION TO CHECK WHETHER A GREY WEIGHT OF A MASS EXISTS

def check(element):
    target_index = bisect_left(grey, element)
    if 0 <= target_index < weight_count and grey[target_index] == element:
        return True
    return False


# 1. TO GET THE INPUT

weight_count = int(sys.stdin.readline())
black = list(map(int, sys.stdin.readline().split()))
grey = list(map(int, sys.stdin.readline().split()))
grey.sort()


# 2. TO CONSTRUCT A SUFFIX SUM ARRAY

black_suffix_sum = [black[-1]]
for index in range(weight_count-2, -1, -1):
    black_suffix_sum.append(black_suffix_sum[-1] + black[index])
black_suffix_sum = list(reversed(black_suffix_sum))
black_suffix_sum.append(0)


# 4. TO SOLVE THE PROBLEM
# Assuming we balance a scale of a black weight of mass A, we need grey weights of mass 2 * A and A - Sum of black weights above the weight.

ans = weight_count
for index in range(weight_count):
    weight = black[index]
    weight_to_put = weight - black_suffix_sum[index + 1]
    weight_to_replace = weight * 2
    if check(weight_to_put) and check(weight_to_replace):
        ans = index + 1
        break

print(ans)
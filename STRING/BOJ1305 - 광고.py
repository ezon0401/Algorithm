'''
BOJ 1305 - Advertisement (https://www.acmicpc.net/problem/1305)

A digital signage of length L infinitely repeats an advertising slogan.
A string that indicates the screen of the digital signage at a specific moment is given.
Print a minimum length of the advertising slogan.
'''

import sys


# 1. TO GET THE INPUT

banner_size = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()


# 2. TO CONSTRUCT KMP TABLE
# The string on the banner is always the repeat of the advertising slogan, with its prefix at the end.
# Thus, the minimum length of the slogan is N - kmp_table[N-1].

kmp_table = [0 for index in range(len(sentence))]

compare_index = 0
for main_index in range(1, len(sentence)):
    while compare_index > 0 and sentence[compare_index] != sentence[main_index]:
        compare_index = kmp_table[compare_index - 1] 
    if sentence[compare_index] == sentence[main_index]:
        compare_index += 1
        kmp_table[main_index] = compare_index
        
print(banner_size - kmp_table[banner_size - 1])
'''
BOJ 1786 - (https://www.acmicpc.net/problem/1786)

Two strings T, and P are given.
How many times and where does P appear in T?
'''


# 1. TO GET THE INPUT
# Be mindful that sys.stdin.readline().strip() harm input strings with blanks.

target = input()
pattern = input()


# 2. KMP

count = 0
locations = []

kmp_table = [0 for index in range(len(pattern))]

compare_index = 0
for main_index in range(1, len(pattern)):
    while compare_index > 0 and pattern[compare_index] != pattern[main_index]:
        compare_index = kmp_table[compare_index - 1]
    if pattern[compare_index] == pattern[main_index]:
        compare_index += 1
        kmp_table[main_index] = compare_index

compare_index = 0
for main_index in range(len(target)):
    while compare_index > 0 and pattern[compare_index] != target[main_index]:
        compare_index = kmp_table[compare_index - 1]
    if pattern[compare_index] == target[main_index]:
        compare_index += 1
        if compare_index == len(pattern):
            count += 1
            locations.append(main_index - compare_index + 2)
            compare_index = kmp_table[compare_index - 1]

print(count)
print(" ".join(map(str, locations)))
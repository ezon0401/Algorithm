'''
BOJ 8484 - Triangles (https://www.acmicpc.net/problem/8484)

There is a numerical sequence c and a sequence of queries [a, b] that ask the following:
Is there a triplet of numbers in the sequence c_a ... c_b so that there is a triangle whose side lengths are those numbers?
If there is a triplet, print TAK. Otherwise, print NIE.
'''

import sys


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. A FUNCTION TO DETERMINE WHETHER THERE IS A TRIPLET

def triangle(num1, num2, num3):
    
    longest = max(num1, num2, num3)
    if num1 + num2 + num3 - longest > longest:
        return True
    else:
        return False


# 3. TO ANSWER THE QUERIES

# If the length of sub-array < 3, there cannot be a triplet.
# There can be no triplet in a sorted sub-array S if S[i] + S[i+1] <= S[i+2] for all i.
# Since the maximum number in the sequence is 10 ** 9, there exists a triplet if the length of the sub-array >= 45 (Consider Fibonacci sequence).
# Now, we can use brute force to solve the problem. 

query_count = int(sys.stdin.readline())
for query in range(query_count):
    start, end = map(int, sys.stdin.readline().split())
    size = end - start + 1
    if size < 3:
        print("NIE")
    elif size >= 45:
        print("TAK")
    else:
        ans = "NIE"
        sub_array = arr[start-1:end]
        for idx1 in range(len(sub_array)):
            for idx2 in range(idx1+1, len(sub_array)):
                for idx3 in range(idx2+1, len(sub_array)):
                    if triangle(sub_array[idx1], sub_array[idx2], sub_array[idx3]):
                        ans = "TAK"
                        break
        print(ans)
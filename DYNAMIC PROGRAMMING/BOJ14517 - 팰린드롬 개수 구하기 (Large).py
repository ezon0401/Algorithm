'''
BOJ 14517 - The number of palindromes (Large) (https://www.acmicpc.net/problem/14517)

Given a string S, calculate the number of palindrome subsequences of S.
'''

import sys

# 1. TO GET THE INPUT

mod = 10007

string = sys.stdin.readline().strip()
length = len(string)


# 2. DYNAMIC PROGRAMMING
# dp[start][end] = The number of palindrome subsequences of S[start:end+1]

dp = [[0 for end in range(length)] for start in range(length)]

for interval in range(length):
    for start in range(length-interval):
        
        if interval == 0:
            dp[start][start+interval] = 1
        else:
            dp[start][start+interval] = dp[start+1][start+interval] + dp[start][start+interval-1] 
            if string[start] == string[start+interval]:
                dp[start][start+interval] += 1
            else:
                dp[start][start+interval] -= dp[start+1][start+interval-1]
        
        dp[start][start+interval] %= mod

print(dp[0][-1])
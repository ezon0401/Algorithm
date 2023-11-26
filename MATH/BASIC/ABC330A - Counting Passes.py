'''
ABC330A - Counting Passes (https://atcoder.jp/contests/abc330/tasks/abc330_a)

N students took a test. They need to get at least L points to pass the exam.
How many students passed the test?
'''

import sys


# 1. TO SOLVE THE PROBLEM

student_count, pass_score = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

count = 0
for score in scores:
    if score >= pass_score:
        count += 1
print(count)
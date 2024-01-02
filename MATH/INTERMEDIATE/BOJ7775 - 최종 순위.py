'''
BOJ 7775 - Ranking (https://www.acmicpc.net/problem/7775)

There are N students.
The sum of the test scores of N students is equal to P. The distinct number of scores of top K students is equal to D. 
Given N, P, K, and D, print a possible score of all students. If there is no possible case, print "Wrong information".
'''

import sys


# 1. TO GET THE INPUT

student_count, total_score, top_count, distinct_count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

if distinct_count == 1:
    
    ans = [total_score // top_count for student in range(top_count)]
    
    if (student_count - top_count) * (total_score // top_count) >= total_score - sum(ans):
        
        left_score = total_score - sum(ans)
        left_student = student_count - top_count
        while left_student > 0:
            score = min(total_score // top_count, left_score)
            ans.append(score)
            left_score -= score
            left_student -= 1
        ans.sort(reverse=True)
        for score in ans:
            print(score)
            
    else:
        print("Wrong information")
        
else:
    
    # The easiest way is to make the sum of the test scores of top K students P.
    # Then, we can fill the other scores to 0.
    ans = [score for score in range(distinct_count)]
    
    if sum(ans) > total_score:
        print("Wrong information")
    else:
        ans[-1] += total_score - sum(ans)
        ans += [0 for student in range(student_count - top_count)]
        ans.sort(reverse=True)
        for score in ans:
            print(score)
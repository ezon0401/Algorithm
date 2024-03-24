'''
BOJ 31558 - Majority Opinion (https://www.acmicpc.net/problem/31558)

There is an array A. You can do the following operation as much as you want. 

(1) Choose two indices i and j.
(2) If there is an element x that appears more than half of sub-array A[i:j+1], all elements from A[i] to A[j] changes to x.

Determine whether you can make all elements equal. If possible, print possible elements. 
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    cow_count = int(sys.stdin.readline())
    cow_preference = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    # If there is an element, the element is the answer.
    if cow_count == 1:

        print(cow_preference[0])
    
    # If there are two elements, they have to be the same.
    elif cow_count == 2:
        
        if cow_preference[0] == cow_preference[1]:
            print(cow_preference[0])
        else:
            print(-1)
    
    # If there are more than two elements, if an element X appears more than twice in A[i:i+3] for any i, it is possible to make every element X.
    else:
        
        possible_case = set()
        
        for start in range(cow_count - 2):
            hayA, hayB, hayC = cow_preference[start:start+3]
            if hayA == hayB or hayA == hayC:
                possible_case.add(hayA)
            elif hayB == hayC:
                possible_case.add(hayB)
        
        possible_case = list(possible_case)
        possible_case.sort()
        
        if len(possible_case) == 0:
            print(-1)
        else:
            print(" ".join(map(str, possible_case)))
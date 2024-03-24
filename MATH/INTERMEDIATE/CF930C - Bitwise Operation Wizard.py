'''
CF930C - Bitwise Operation Wizard (https://codeforces.com/contest/1937/problem/C)

There is a secret sequence S, which is a permutation of {0, 1, ..., n-1}.
You can pick four arbitrary indices and ask for the comparison result between S[A] | S[B] and S[C] | S[D].
Print two indices so that S[i] ^ S[j] is the possible maximum value.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    size = int(sys.stdin.readline())
    
    
    # 2. TO FIND THE LARGEST VALUE X
    
    max_index = 0
    
    for index in range(1, size):
        print("? {} {} {} {}".format(max_index, max_index, index, index))
        sys.stdout.flush()
        result = sys.stdin.readline().strip()
        if result == "<":
            max_index = index


    # 3. TO FIND VALUES Y SO THAT X | Y == 11...1

    key_index = 0
    keys = [0]
    
    for index in range(1, size):
        print("? {} {} {} {}".format(max_index, key_index, max_index, index))
        sys.stdout.flush()
        result = sys.stdin.readline().strip()
        if result == "<":
            key_index = index
            keys = [index]
        elif result == "=":
            keys.append(index)
    
    
    # 4. TO FIND THE SMALLEST Y
    
    min_index = keys[0]
    
    for index in range(1, len(keys)):
        print("? {} {} {} {}".format(min_index, min_index, keys[index], keys[index]))
        sys.stdout.flush()
        result = sys.stdin.readline().strip()
        if result == ">":
            min_index = keys[index]
    
    
    # 5. TO SOLVE THE PROBLEM
    
    print("! {} {}".format(max_index, min_index))
    sys.stdout.flush()
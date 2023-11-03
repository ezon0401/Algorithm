'''
BOJ 25957 - Word Superiority Effect (by Cambridge University) (https://www.acmicpc.net/problem/25957)

There is a sentence C consists of N words.
However, for each word in C, the order of characters may be muddled except for the first and the last characters.
Restore the sentence.
'''

import sys


# 1. A FUNCTION TO CONVERT WORD INTO KEY

def word_to_key(word):
    
    char_list = list(word)
    
    if len(word) > 3:
    
        start = [char_list[0]]
        middle = char_list[1:-1]
        end = [char_list[-1]]
        middle.sort()
        
        char_list = start + middle + end
    
    return "".join(char_list)
    

# 2. TO CONSTRUCT A CONVERT TABLE

convert_table = {}

word_count = int(sys.stdin.readline())

for word_input in range(word_count):
    
    word = sys.stdin.readline().strip()
    key = word_to_key(word)
    
    convert_table[key] = word


# 3. TO SOLVE THE PROBLEM

word_total_count = int(sys.stdin.readline())
sentence = list(sys.stdin.readline().strip().split())

for index in range(word_total_count):
    word = sentence[index]
    sentence[index] = convert_table[word_to_key(word)]
    
print(" ".join(sentence))
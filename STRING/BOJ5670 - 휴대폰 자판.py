'''
BOJ 5670 - Phone Keyboard (https://www.acmicpc.net/problem/5670)

A phone is using an English dictionary with limited words. 
If there is only one possible next character, the phone will auto-complete the character.
What is the average number of presses needed to complete each character?
'''

import sys


# 2. TRIE

class Node:
    
    def __init__(self, character, data=None):
        self.character = character
        self.data = data
        self.children = {}

class Trie:
    
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, word):
        now = self.root
        for char in word:
            if char not in now.children:
                now.children[char] = Node(char)
            now = now.children[char]
        now.data = word
    
    def press_count(self, word):
        now = self.root
        count = 0
        for char in word:
            if now == self.root or len(now.children) != 1 or (now.data != None and now.data != word):
                count += 1
            now = now.children[char]
        return count


# 1. TO GET INPUT

while True:
    
    try:
        word_count = int(sys.stdin.readline())
    except:
        break

    words = []
    for word_input in range(word_count):
        word = sys.stdin.readline().strip()
        words.append(word)


    # 3. TO SOLVE THE PROBLEM

    trie = Trie()
    
    for word in words:
        trie.insert(word)
        
    total_press = 0
    for word in words:
        total_press += trie.press_count(word)
    
    print(format(total_press / word_count, ".2f"))

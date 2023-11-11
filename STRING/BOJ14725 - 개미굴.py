'''
BOJ 14725 - Ant Nest (https://www.acmicpc.net/problem/14725)

A robot ant traverses an ant nest and sends information.
Each line of information represents a distinct path from top to bottom.
Print the structure of the nest.
'''

import sys


# 1. TRIE

class Node:
    
    def __init__(self, element, data=None):
        
        self.element = element
        self.data = data
        self.children = {}
    
class Trie:
    
    def __init__(self):
        
        self.root = Node(None)
    
    def insert(self, array):
        
        now = self.root
        for element in array:
            if element not in now.children:
                now.children[element] = Node(element)
            now = now.children[element]
        now.data = array


# 3. A FUNCTION TO SEARCH TRIE (DFS)

def dfs(now, depth):
    
    children = sorted(now.children.keys())
    
    for child in children:
        print("--" * depth + now.children[child].element)
        dfs(now.children[child], depth + 1)


# 2. TO GET THE INPUT

info_count = int(sys.stdin.readline())

trie = Trie()

for info_input in range(info_count):
    info = list(sys.stdin.readline().strip().split())[1:]
    trie.insert(info)


# 4. TO SOLVE THE PROBLEM

dfs(trie.root, 0)

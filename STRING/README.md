# String

This repository introduces advanced-level algorithms regarding string.

## KMP

KMP algorithm checks whether string X is a substring of string S in O(|X| + |S|) time complexity. 

The key idea is a failure function. The failure function eliminates the redundant comparison by storing how many indices have matched.

*Application*

* The i-th index of kmp_table equals to i - the length of the longest repeated substring.

*Sample Code*
```python
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
            compare_index = kmp_table[compare_index - 1]
```

## Trie

Trie is a tree specialized for string search. If there are X words and the longest word is a length of L, the time complexity for constructing Trie is O(XL) and searching a word is O(L).

*Sample Code*
```python
class Node:
    
    def __init__(self, char, word=None):
        
        self.char = char
        self.word = word
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
        now.word = word

    def search(self, word):

        now = self.root
        for char in word:
            if char not in now.children:
                return False
            else:
                now = now.children[char]
        
        if now.word == word:
            return True
```

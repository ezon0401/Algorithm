'''
BOJ 7247 - Encryption (https://www.acmicpc.net/problem/7247)

The text is encrypted according to the following rules.

(1) A-Z corresponds with 1 to 26. '_' corresponds with 27, ',' corresponds with 28, and '.' corresponds with 29.
(2) Let's assume char(x) converts a number to the corresponding character, and num(x) converts a character to the corresponding number.
    Then, character S in the original text corresponds with char((num(S) ^ 3 % 29) + 1) in the encrypted text. 

Decrypt the encrypted text. 
'''

import sys


# 1. CONSTRUCT A DECRYPTION TABLE

# To create a map that converts a number to the corresponding character and a character to the corresponding number.

conversion_table = {}

for char_ascii in range(65, 91):
    conversion_table[char_ascii - 64] = chr(char_ascii)
    conversion_table[chr(char_ascii)] = char_ascii - 64

conversion_table[27] = "_"
conversion_table["_"] = 27
conversion_table[28] = ","
conversion_table[","] = 28
conversion_table[29] = "."
conversion_table["."] = 29

# To create a map that converts an encrypted number to the corresponding original number.

decryption_table = {}

for original_num in range(1, 30):
    
    encrypted_num = (original_num ** 3) % 29 + 1
    decryption_table[encrypted_num] = original_num
    

# 2. TO SOLVE THE PROBLEM

code = sys.stdin.readline().strip()
original_text = ""

for character in code:
    original_text += conversion_table[decryption_table[conversion_table[character]]]
print(original_text)
'''
BOJ 16246 - Magic Weapon (https://www.acmicpc.net/problem/16246)

Magic weapon requires a green part, a red part, and a blue part.
Each part has a model number, and the following three rules should be satisfied to create the magic weapon.

(1) The first digit of the model number of the red part equals to the last digit of the model number of the green part.
(2) The last digit of the model number of the red part equals to the first digit of the model number of the blue part.
(3) Model numbers of all three parts are different.

How many different ways are there to create the magic weapon?
'''

import sys


# 2. FUNCTIONS TO CHECK THE NUMBER OF CASES

# The number of cases after considering duplication when the model number of a red detail starts with red_start and ends with red_end

def count_case(red_start, red_end):
    
    return total_with_duplicate(red_start, red_end) - duplicate_two(red_start, red_end) + duplicate_three(red_start, red_end) * 2

# The number of models to consider on each color when the start and end digits of a red model are given. 

def color_count(red_start, red_end):
    
    green_count = 0
    for start in range(10):
        green_count += sum(green[start][red_start].values())
    red_count = sum(red[red_start][red_end].values())
    blue_count = 0
    for end in range(10):
        blue_count += sum(blue[red_end][end].values())
    
    return green_count, red_count, blue_count

# The number of possible combinations of model numbers without considering duplications

def total_with_duplicate(red_start, red_end):
    
    green_count, red_count, blue_count = color_count(red_start, red_end)
    
    return green_count * red_count * blue_count
    
# The number of cases when two or three model numbers are duplicated

def duplicate_two(red_start, red_end):
    
    green_count, red_count, blue_count = color_count(red_start, red_end)
    
    duplicate = 0
    
    if red_start == red_end:
        for green_red in list(set(green[red_start][red_end]) & set(red[red_start][red_end])):
            duplicate += green[red_start][red_end][green_red] * red[red_start][red_end][green_red] * blue_count
        for red_blue in list(set(red[red_start][red_end]) & set(blue[red_start][red_end])):
            duplicate += green_count * red[red_start][red_end][red_blue] * blue[red_start][red_end][red_blue]
    for green_blue in list(set(green[red_end][red_start]) & set(blue[red_end][red_start])):
        duplicate += green[red_end][red_start][green_blue] * red_count * blue[red_end][red_start][green_blue]
    
    return duplicate

# The number of cases when all three model numbers are duplicated

def duplicate_three(red_start, red_end):

    duplicate = 0
    
    if red_start == red_end:
        for green_red_blue in list(set(green[red_start][red_end]) & set(red[red_start][red_end]) & set(blue[red_start][red_end])):
            duplicate += green[red_start][red_end][green_red_blue] * red[red_start][red_end][green_red_blue] * blue[red_start][red_end][green_red_blue]
        
    return duplicate


# 1. TO GET THE INPUT

import sys

green_count, red_count, blue_count = map(int, sys.stdin.readline().split())

green = [[{} for green_end in range(10)] for green_start in range(10)]
red = [[{} for red_end in range(10)] for red_start in range(10)]
blue = [[{} for blue_end in range(10)] for blue_start in range(10)]

green_models = list(sys.stdin.readline().strip().split())
for green_model in green_models:
    green_start = int(green_model[0])
    green_end = int(green_model[-1])
    green[green_start][green_end][int(green_model)] = green[green_start][green_end].get(int(green_model), 0) + 1

red_models = list(sys.stdin.readline().strip().split())
for red_model in red_models:
    red_start = int(red_model[0])
    red_end = int(red_model[-1])
    red[red_start][red_end][int(red_model)] = red[red_start][red_end].get(int(red_model), 0) + 1

blue_models = list(sys.stdin.readline().strip().split())
for blue_model in blue_models:
    blue_start = int(blue_model[0])
    blue_end = int(blue_model[-1])
    blue[blue_start][blue_end][int(blue_model)] = blue[blue_start][blue_end].get(int(blue_model), 0) + 1
    

# 3. TO SOLVE THE PROBLEM

ans = 0

for red_start in range(10):
    for red_end in range(10):
        ans += count_case(red_start, red_end)
print(ans)

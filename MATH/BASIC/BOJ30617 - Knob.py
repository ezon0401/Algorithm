'''
BOJ 30617 - Knob (https://www.acmicpc.net/problem/30617)

Sung-woo is playing a rhythm game.
There are a left knob and a right knob. Each knob can be rotated clockwise and anti-clockwise. How to rotate each knob is given.

The fun of a song increases by 1 when the following condition is satisfied:
(1) Rotate a knob in the same direction twice, consecutively.
(2) Rotate both knobs in the same direction.

Determine the fun of the song. 
'''

import sys


# 2. A FUNCTION TO GET HOW MUCH FUN INCREASES FROM A KNOB

def knob_fun(knob):    
    
    fun = 0
    for index in range(1, song_length):
        if knob[index] == knob[index-1] and knob[index] != 0:
            fun += 1
    return fun
    

# 1. TO GET THE INPUT

song_length = int(sys.stdin.readline())

left_knob = []
right_knob = []

for note in range(song_length):
    left, right = map(int, sys.stdin.readline().split())
    left_knob.append(left)
    right_knob.append(right)


# 3. TO SOLVE THE PROBLEM

fun = 0
fun += knob_fun(left_knob)
fun += knob_fun(right_knob)

for index in range(song_length):
    if left_knob[index] == right_knob[index] and left_knob[index] != 0:
        fun += 1

print(fun)
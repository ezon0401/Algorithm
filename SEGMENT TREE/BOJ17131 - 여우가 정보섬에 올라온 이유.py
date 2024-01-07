'''
BOJ 17131 - The Reason Why A Fox Climbed Informatics Island (https://www.acmicpc.net/problem/17131)

If s_x < t_x < u_x and s_y > t_y < u_y, the stars (s, t, u) construct a V constellation.
Given the coordinates of stars, determine the number of possible V constellations.
'''

import sys


# 3. FUNCTIONS TO PROCESS SEGMENT TREES

def delete(star):
    
    x, y = star
    y += align + convert
    
    while y != 0:
        left_seg[y] -= 1
        y >>= 1
    
def add(star):
    
    x, y = star
    y += align + convert
    
    while y != 0:
        right_seg[y] += 1
        y >>= 1
    

# 4. FUNCTIONS TO COUNT THE NUMBER OF V CONSTELLATIONS

# Count the number of stars above
def count_above(seg_tree, star):
    
    x, y = star
    y += align + convert
    
    count = 0
    
    start = y + 1
    end = (1 << 20) - 1
    while start <= end:
        if start % 2 == 1:
            count += seg_tree[start]
            start += 1
        if end % 2 == 0:
            count += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return count

# Count the number of V constellations
def count_V(star):
    
    x, y = star
    
    left = count_above(left_seg, star) % mod
    right = count_above(right_seg, star) % mod
    
    return (left * right) % mod
    

# 1. TO GET THE INPUT

mod = 10 ** 9 + 7

star_count = int(sys.stdin.readline())
stars = []
for star_input in range(star_count):
    x, y = map(int, sys.stdin.readline().split())
    stars.append((x, y))
stars.sort()


# 2. TO CONSTRUCT SEGMENT TREES

align = (1 << 19) - 1
convert = 200001

left_seg = [0 for index in range(1 << 20)]
right_seg = [0 for index in range(1 << 20)]

for x, y in stars:
    y += align + convert
    while y != 0:
        left_seg[y] += 1
        y >>= 1


# 5. TO SOLVE THE PROBLEM

ans = 0
wait = []

while stars:
    now_star = stars.pop()
    if len(wait) != 0 and wait[-1][0] != now_star[0]:
        for star_to_count in wait:
            ans = (ans + count_V(star_to_count)) % mod
        while wait:
            add(wait.pop())
    delete(now_star)
    wait.append(now_star)
    
print(ans)

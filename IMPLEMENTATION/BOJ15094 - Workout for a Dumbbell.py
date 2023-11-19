'''
BOJ 15094 - Workout for a Dumbbell (https://www.acmicpc.net/problem/15094)

Jim cycles through a sequence of 10 machines three times for his workout.
He has fixed usage time and recovery time for each machine.
There are 10 other people in the gym using one of the 10 machines exclusively.
They also have fixed usage time and recovery time for a machine.

Jim and the other members cannot use a machine at the same time.
How long Jim's workout would take?
'''

import sys


# 2. A FUNCTION TO CALCULATE HOW LONG A CYCLE TAKES

def cycle(start):
    
    now = start
    
    for machine in range(10):
        
        jim_time, jim_recovery = jim[machine]
        member_time, member_recovery, member_start = gym[machine]
        
        if member_start > now:
            
            # If the member has not started using the machine
            jim_end = now + jim_time
            if jim_end >= member_start:
                gym[machine][2] = jim_end
            now = jim_end + jim_recovery
            
        else:
            
            member_status = (now - member_start) % (member_time + member_recovery) 
            
            # If the member is recovering
            if member_time <= member_status:
                jim_end = now + jim_time
                if member_status - member_time + jim_time >= member_recovery:
                    gym[machine][2] = jim_end % (member_time + member_recovery)
                now = jim_end + jim_recovery
            
            # If the member is using the machine 
            else:
                jim_end = now + member_time - member_status + jim_time
                if jim_time >= member_recovery:
                    gym[machine][2] = jim_end % (member_time + member_recovery)
                now = jim_end + jim_recovery
            
    return now
    

# 1. TO GET THE INPUT

jim = [[0, 0] for machine in range(10)]
gym = [[0, 0, 0] for machine in range(10)]

jim_input = list(map(int, sys.stdin.readline().split()))
for index in range(0, 20, 2):
    jim[index // 2] = [jim_input[index], jim_input[index + 1]]

for member in range(10):
    time, recovery, start = map(int, sys.stdin.readline().split())
    gym[member] = [time, recovery, start]


# 3. TO SOLVE THE PROBLEM

start = 0
first = cycle(start)
second = cycle(first)
final = cycle(second)
print(final - jim[-1][1])
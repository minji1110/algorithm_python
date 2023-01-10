import sys
def input(): return sys.stdin.readline().rstrip()

n=int(input())
fear = list(map(int, input().split()))

fear.sort()

group=0
pointer=-1
this_group=0

while(pointer+1<len(fear)):
    pointer+=1
    this_group+=1
    num_of_min = fear[pointer]

    if this_group>=num_of_min:
        group+=1
        this_group=0
    

print(group)
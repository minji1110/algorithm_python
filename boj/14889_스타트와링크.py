import sys
from itertools import combinations
def input(): return sys.stdin.readline().rstrip()

n=int(input())
members=set([i for i in range(n)])
skill=[]
for _ in range(n):
    skill.append(list(map(int,input().split())))

answer=1e9
combi=list(combinations(members,n//2))
for c in range(len(combi)//2):
    start=set(combi[c])
    link=members-start

    start_sum=0
    for i in start:
        for j in start:
            start_sum+=skill[i][j]
    link_sum=0
    for i in link:
        for j in link:
            link_sum+=skill[i][j]
    
    answer=min(answer,abs(start_sum-link_sum))
print(answer)
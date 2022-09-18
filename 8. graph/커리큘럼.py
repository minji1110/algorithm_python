import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

n=int(input())
graph=[[] for _ in range(n+1)]
indegree_table = [0] * (n+1)
time_table=[0] * (n+1) # 과목 듣는 소요시간
total_time_table = [0] * (n+1) # 선수과목~ 에서 소요되는 총 시간

for i in range(1,n+1):
    inputs=list(map(int, input().split()))
    time_table[i]=int(inputs[0])

    for prev in range(1, len(inputs)-1):
        need_to_prev = inputs[prev]
        graph[need_to_prev].append(i)
        indegree_table[i]+=1

q=deque()
for i in range(1,n+1):
    if indegree_table[i]==0:
        q.append(i)
        total_time_table[i]=time_table[i]

while q:
    v=q.popleft()

    for adjacent in graph[v]:
        indegree_table[adjacent]-=1 # 진입차수 감소
        total_time_table[adjacent] = max(total_time_table[adjacent],total_time_table[v])

        if indegree_table[adjacent]==0:
            q.append(adjacent)
            total_time_table[adjacent]+=time_table[adjacent]

for i in range(1,n+1):
    print(total_time_table[i])
        


    
    



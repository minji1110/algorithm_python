import sys
from collections import deque
def input() : return sys.stdin.readline().rstrip()

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)

q=deque()
q.append((X,0)) #노드, 거리
visited[X]=True

answer=[]
while q:
    v,dis=q.popleft()
    if dis==K:
        answer.append(v)
    elif dis>K:
        break
    for adj in graph[v]:
        if not visited[adj]:
            q.append((adj,dis+1))
            visited[adj]=True

if not answer:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)

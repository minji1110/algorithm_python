import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n,m,k,start=map(int, input().split())
adjacent=[ [] for _ in range(n+1)]
visited=[False for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    adjacent[a].append(b)

q=deque()
q.append((start,0))
visited[start]=True

cnt=0
while(q):
    v,distance=q.popleft()
    if distance == k:
        print(v)
        cnt+=1
    elif distance>k:
        break
    else:
        for u in adjacent[v]:
            if not visited[u]:
                visited[u]=True
                q.append((u,distance+1))

if cnt==0:
    print(-1)
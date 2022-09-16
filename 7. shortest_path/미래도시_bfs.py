import sys
from collections import deque
def input() : return sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # 회사의 수, 경로의 수
matrix=[[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int , input().split())
    matrix[v1][v2]=matrix[v2][v1]=True

dest2, dest1 = map(int, input().split())
visited=[False] * (n+1)

def bfs(start, end):
    q=deque()
    q.append((start,0))

    while q:
        v, weight = q.popleft()
        for i in range(1,n+1):
            if matrix[v][i] and not visited[i]:
                visited[i]=True
                q.append((i,weight+1))
                if i==end : return weight+1

    return -1


distance1 = bfs(1,dest1)
visited=[False] * (n+1)
distance2 = bfs(dest1, dest2)

if(distance1==-1 or distance2==-1): print(-1)
else: print(distance1+distance2)
from collections import deque

n=int(input())
a,b=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(int(input())):
    parent,child=map(int,input().split())
    graph[parent].append(child)
    graph[child].append(parent)

q=deque()
q.append((a,0))
visited[a]=True 

found=False
while q:
    x,count =q.popleft()
    if x==b:
        found=True
        print(count)
        break
    for adj in graph[x]:
        if not visited[adj]:
            q.append((adj,count+1))
            visited[adj]=True

if not found: 
    print(-1)

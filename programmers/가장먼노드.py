from collections import deque

def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n)]
    visited=[False]*n
    
    for a,b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    q=deque()
    q.append((0,0))
    visited[0]=True
    
    maximum=0
    while q:
        v,dis=q.popleft()
        if dis>maximum:
            maximum=dis
            answer=1
        elif dis==maximum:
            answer+=1
        for adj in graph[v]:
            if not visited[adj]:
                q.append((adj,dis+1))
                visited[adj]=True
    
    return answer
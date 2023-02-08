from collections import deque

def bfs(n,computers,start,visited):
    q=deque()

    visited[start]=True
    q.append(start)

    while(q):
        x=q.popleft()
        for i in range(n):
            if  not visited[i] and computers[x][i]==1:
                visited[i]=True
                q.append(i)

def solution(n, computers):
    answer = 0
    visited=[False]*n 
    
    for i in range(n):
        if not visited[i]:
            answer+=1
            bfs(n,computers,i,visited)
    return answer

n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))
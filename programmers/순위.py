from collections import deque

def simulate(matrix, i):
    visited=[False]*(len(matrix))
    q=deque()
    visited[i]=True
    for k in range(1,len(matrix)):
        if matrix[i][k]!=0:
            q.append((k,matrix[i][k]))
            visited[k]=True
    
    count=1
    while q:
        x,win_or_lose=q.popleft()
        count+=1
        for y in range(1,len(matrix)):
            if not visited[y] and matrix[x][y]==win_or_lose:
                q.append((y,win_or_lose))
                visited[y]=True 
    return count==len(matrix)-1 #count==n
            
def solution(n, results):
    answer = 0
    matrix=[[0]*(n+1) for _ in range(n+1)]
    for winner,loser in results:
        matrix[winner][loser]=1
        matrix[loser][winner]=-1
    
    for i in range(1,n+1):
        if simulate(matrix, i): answer+=1
    return answer
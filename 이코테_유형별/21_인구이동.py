import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dx=[0,0,1,-1]
dy=[1,-1,0,0]
states=[]

N,L,R = map(int,input().split())
for _ in range(N):
    states.append(list(map(int,input().split())))
visited=[[False]*N for _ in range(N)]

# 연합
def unite(start_r,start_c):
    total_population=0
    united=[]
    q=deque()
    
    visited[start_r][start_c]=True
    total_population+=states[start_r][start_c]
    q.append((start_r,start_c))
    united.append((start_r,start_c))

    while q:
        r,c=q.popleft()
        for i in range(4):
            nr,nc=r+dx[i],c+dy[i]
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc] and L<=abs(states[r][c]-states[nr][nc])<=R:
                    visited[nr][nc]=True
                    total_population+=states[nr][nc]
                    q.append((nr,nc))
                    united.append((nr,nc))
    
    if len(united)==1:
        return False

    # 연합 인구수 조정    
    united_population = total_population//len(united)
    for x,y in united:
        states[x][y]=united_population

    return True


days=0
while True:
    can_be_united=False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if(unite(r,c)):
                    can_be_united=True
    
    if not can_be_united:
        break
    
    days+=1
    for i in range(N):
        for j in range(N):
            visited[i][j]=False

print(days)



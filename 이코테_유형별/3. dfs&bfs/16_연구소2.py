import sys
import copy
from itertools import combinations
from collections import deque
def input() : return sys.stdin.readline().rstrip()

# 바이러스 확산
def spread_virus():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visited=[[False]*M for _ in range(N)]
    lab_copy=copy.deepcopy(lab)
    
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j]==2 and not visited[i][j]:
                q=deque()
                q.append((i,j))
                visited[i][j]=True

                while q:
                    x,y=q.popleft()
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<N and 0<=ny<M:
                            if lab_copy[nx][ny]!=1 and not visited[nx][ny]:
                                lab_copy[nx][ny]=2
                                visited[nx][ny]=True
                                q.append((nx,ny))                
    return lab_copy

# 안전영역 크기 구하기
def count_safe_area(lab_copy):
    cnt=0
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j]==0:
                cnt+=1
    return cnt

# 0:빈칸, 1:벽, 2:바이러스
N,M=map(int,input().split())
lab=[]
for _ in range(N):
    lab.append(list(map(int,input().split())))

answer=0
for a, b, c in (list(combinations(range(N*M),3))): # a,b,c번째 칸
    ax,ay=a//M,a%M
    bx,by=b//M,b%M
    cx,cy=c//M,c%M

    if lab[ax][ay]==lab[bx][by]==lab[cx][cy]==0:
        # 벽 세우기
        lab[ax][ay],lab[bx][by],lab[cx][cy]=1,1,1
        
        spreaded=spread_virus()
        safe_area=count_safe_area(spreaded)
        answer=max(answer,safe_area)
        
        # 원상복귀
        lab[ax][ay],lab[bx][by],lab[cx][cy]=0,0,0
print(answer)
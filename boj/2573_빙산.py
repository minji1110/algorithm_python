from collections import deque

N,M=map(int,input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
to_be_melted=[]

#연결 리스트의 개수를 센다.
def count_linked_list():
    global to_be_melted
    
    visited=[[False]*M for _ in range(N)]
    to_be_melted=[]
    count=0
    q=deque()

    for i in range(N):
        for j in range(M):
            if matrix[i][j]>0 and not visited[i][j]:
                count+=1
                q.append((i,j))
                visited[i][j]=True

                while q:
                    x,y=q.popleft()
                    melt_amount=0
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<N and 0<=ny<M:
                            if matrix[nx][ny]==0: # 인접한칸이 0
                                melt_amount+=1
                                continue
                            if not visited[nx][ny]:  # 인접한칸이 빙산
                                q.append((nx,ny))
                                visited[nx][ny]=True
                    
                    if melt_amount>0:
                        to_be_melted.append((x,y,melt_amount))
    return count

# 빙산이 녹음.
def melts():
    for x,y,amount in to_be_melted:
        matrix[x][y]=max(0,matrix[x][y]-amount)

year=0
while True:
    cnt_of_linked_list=count_linked_list() #연결리스트 개수
    
    if cnt_of_linked_list>=2:
        print(year)
        break
    elif cnt_of_linked_list==0:
        print(0)
        break

    year+=1
    melts()
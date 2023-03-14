from collections import deque

# 좌,하,우,상
dx=[0,1,0,-1]
dy=[-1,0,1,0]

A=[]
init_amount=0
N=int(input())

for _ in range(N):
    data=list(map(int,input().split()))
    A.append(data)
    init_amount+=sum(data)

dir_q=deque()
for k in range(1,N):
    if k%2==1:
        for _ in range(k):
            dir_q.append(0) #좌
        for _ in range(k):
            dir_q.append(1) #하
    else:
        for _ in range(k):
            dir_q.append(2)
        for _ in range(k):
            dir_q.append(3)

for _ in range(N):
    dir_q.append(0)

# 모래 이동
def spread_sand(x,y,nx,ny,d):    
    total_sand=A[nx][ny]
    A[nx][ny]=0
    accumulated=0
    
    spread_x,spread_y=[],[]
    spread_rate=[1,1,2,2,7,7,10,10,5]

    if x==nx: # 좌우
        spread_x=[x-1,x+1,x-2,x+2,x-1,x+1,x-1,x+1,x,x]
        spread_y=[y,y,ny,ny,ny,ny,ny+dy[d],ny+dy[d],ny+2*dy[d],ny+dy[d]]
        
    else: # 상하
        spread_x=[x,x,nx,nx,nx,nx,nx+dx[d],nx+dx[d],nx+2*dx[d],nx+dx[d]]
        spread_y=[y-1,y+1,y-2,y+2,y-1,y+1,y-1,y+1,y,y]
    
    for i in range(9):
        sx,sy=spread_x[i],spread_y[i]
        amount=(spread_rate[i]*total_sand)//100
        accumulated+=amount

        if 0<=sx<N and 0<=sy<N:
            A[sx][sy]+=amount
    
    sx,sy=spread_x[9],spread_y[9]
    alpha_amount=total_sand-accumulated
    if 0<=sx<N and 0<=sy<N:
        A[sx][sy]+=alpha_amount
        
# main
now_x,now_y=N//2,N//2
while dir_q:
    d=dir_q.popleft()
    nx,ny=now_x+dx[d],now_y+dy[d]

    if A[nx][ny]>0:
        spread_sand(now_x,now_y,nx,ny,d)
    now_x,now_y=nx,ny

rest=0
for row in range(N):
    rest+=sum(A[row])
print(init_amount-rest)
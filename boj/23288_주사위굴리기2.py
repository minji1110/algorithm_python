from collections import deque

N,M,K=map(int,input().split())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dice=[[-1,2,-1],[4,1,3],[-1,5,-1],[-1,6,-1]] #전개도
now_dir=0 #방향
now_x,now_y=0,0 #위치

# 동,북,서,남
dx=[0,-1,0,1]
dy=[1,0,-1,0]

# 주사위 아랫면의 정수를 반환
def get_bottom_value():
    global dice
    return dice[3][1]

# 전개도를 설정
def set_dice():
    global dice,now_dir
    if now_dir==0: #동 
        dice[1][1],dice[1][2],dice[3][1],dice[1][0]=dice[1][0],dice[1][1],dice[1][2],dice[3][1]
    elif now_dir==1: #북
        dice[3][1],dice[0][1],dice[1][1],dice[2][1]=dice[0][1],dice[1][1],dice[2][1],dice[3][1]
    elif now_dir==2: #서
        dice[3][1],dice[1][0],dice[1][1],dice[1][2]=dice[1][0],dice[1][1],dice[1][2],dice[3][1]
    else: #남
        dice[1][1],dice[2][1],dice[3][1],dice[0][1]=dice[0][1],dice[1][1],dice[2][1],dice[3][1]

# 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
def roll_dice():
    global now_x,now_y,now_dir
    
    nx,ny=now_x+dx[now_dir],now_y+dy[now_dir]
    if not (0<=nx<N and 0<=ny<M):
        now_dir=(now_dir+2)%4
        nx,ny=now_x+dx[now_dir],now_y+dy[now_dir]
    
    set_dice()
    now_x,now_y=nx,ny

#점수를 계산
def calculate_score(B):
    visited=[[False]*M for _ in range(N)]
    q=deque()

    visited[now_x][now_y]=True
    q.append((now_x,now_y))

    C=0
    while q:
        x,y=q.popleft()
        C+=1

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and matrix[nx][ny]==B:
                visited[nx][ny]=True
                q.append((nx,ny))
    
    return B*C
    
score=0 #점수
for _ in range(K):
    roll_dice()
    
    A=get_bottom_value()
    B=matrix[now_x][now_y]
    
    score+=calculate_score(B) # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.

    if A>B:
        now_dir=(now_dir-1)%4 # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    elif A<B:
        now_dir=(now_dir+1)%4 # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    
print(score)
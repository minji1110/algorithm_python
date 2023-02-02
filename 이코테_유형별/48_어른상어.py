import sys
def input(): return sys.stdin.readline().rstrip()

# 상,하,좌,우
dx=[None,-1,1,0,0]
dy=[None,0,0,-1,1]

N,M,k = map(int,input().split())

space = []
smell=[[[-1,-1] for _ in range(N)] for _ in range(N)] # 냄새 정보 [상어번호, 남은시간]
sharks=[[-1]*3 for _ in range(M+1)] # i 번째 상어의 x,y,dir
sharks_priority=[] # i 번째 상어의 방향 우선순위

def set_data():
    for i in range(N):
        space.append(list(map(int,input().split())))
        for j in range(N):
            if space[i][j]>0:
                sharks[space[i][j]]=[i,j,-1]
                smell[i][j]=[space[i][j],k]

    dir= list(map(int,input().split()))
    for i in range(len(dir)):
        sharks[i+1][2]=dir[i]

    for i in range(M):
        i_priority=[]
        i_priority.append([-1,-1,-1,-1])
        for j in range(4):
            i_priority.append(list(map(int,input().split())))
        sharks_priority.append(i_priority)


# 상어의 다음 위치를 설정
def set_next_space(next_space,i):
    x,y,dir=sharks[i]
    priority=sharks_priority[i-1][dir]

    empty_exist=False
    for j in range(4):
        nx,ny=x+dx[priority[j]],y+dy[priority[j]]
        if 0<=nx<N and 0<=ny<N:
            if smell[nx][ny][0]>0 : # 냄새O
                continue
            else: # 냄새 X 
                empty_exist=True
                next_space.append((i,nx,ny,priority[j]))
                break
    
    if not empty_exist:
        for j in range(4):
            nx,ny=x+dx[priority[j]],y+dy[priority[j]]
            if 0<=nx<N and 0<=ny<N and smell[nx][ny][0]==i:
                next_space.append((i,nx,ny,priority[j]))
                break

# 상어 이동
def move(next_space):
    for i,x,y,dir in next_space:
        # 이전 위치 비우기
        prev_x,prev_y=sharks[i][0],sharks[i][1]
        space[prev_x][prev_y]=0

        if space[x][y]==0:
            space[x][y]=i
            smell[x][y]=[i,k]
            sharks[i]=[x,y,dir]

        # 이미 상어 존재
        else:
            delete_shark(i)

# 냄새 -1
def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][0]==-1 or space[i][j]>0:
                continue
            else:
                smell[i][j][1]-=1
                if smell[i][j][1]==0:
                    smell[i][j]=[-1,-1]

# 상어 삭제
def delete_shark(i):
    global rest
    sharks[i][0]=sharks[i][1]=-1 
    rest-=1

set_data()
t=0
rest=M
answer=-1

while True:
    t+=1

    next_space=[] # 각 상어가 다음으로 이동할 위치
    for i in range(1,M+1):
        if sharks[i][0]!=-1:
            set_next_space(next_space,i)
    move(next_space)
    
    update_smell()

    if rest==1:
        answer=t
        break

    if t>=1000:
        break

print(answer)

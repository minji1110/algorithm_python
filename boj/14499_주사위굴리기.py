import sys
def input(): return sys.stdin.readline().rstrip()

#동, 서, 북, 남
dx=[None,0,0,-1,1]
dy=[None,1,-1,0,0]
dice=[[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]

# 주사위 굴리기
def roll_dice(direction):
    if direction==1: #동
        dice[1][0],dice[1][1],dice[1][2],dice[3][1]=dice[3][1],dice[1][0],dice[1][1],dice[1][2]
    elif direction==2: #서
        dice[1][0],dice[1][1],dice[1][2],dice[3][1]=dice[1][1],dice[1][2],dice[3][1],dice[1][0]
    elif direction==3: #북
        dice[0][1],dice[1][1],dice[2][1],dice[3][1]=dice[1][1],dice[2][1],dice[3][1],dice[0][1]
    else: #남
        dice[0][1],dice[1][1],dice[2][1],dice[3][1]=dice[3][1],dice[0][1],dice[1][1],dice[2][1]

N,M,x,y,k=map(int,input().split())
maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))
commands=list(map(int,input().split()))

for i in range(k):
    direction=commands[i]
    nx,ny=x+dx[direction],y+dy[direction]
    
    if not (0<=nx<N and 0<=ny<M):
        continue
    
    roll_dice(direction)
    x,y=nx,ny
    
    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
    if maps[x][y]==0:
        maps[x][y]=dice[3][1]
    else:
        dice[3][1]=maps[x][y]
        maps[x][y]=0
    
    print(dice[1][1]) #윗면
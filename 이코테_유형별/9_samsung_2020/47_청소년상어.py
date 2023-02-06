# 실패 다시
import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

fishes=[[0]*4 for _ in range(4)]
directions=[[0]*4 for _ in range(4)]
fishes_q=[]

# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def fish_move():
    fish,x,y=heapq.heappop(fishes_q)
    dir=directions[x][y]
    
    for _ in range(8):
        nx,ny= x+dx[dir],y+dy[dir]
        if 0<=nx<4 and 0<=ny<4 and fishes[nx][ny]>0: # 교체 가능
            fishes[x][y]=fishes[nx][ny]
            fishes[nx][ny]=fish
            directions[x][y]=directions[nx][ny]
            directions[nx][ny]=dir
            return
        dir=(dir+1)%8

def shark_can_go(x,y,dir):
    can_go_list=[]

    while True:
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<4 and 0<=ny<4 and fishes[nx][ny]>0:
            can_go_list.append((nx,ny))
            x,y=nx,ny
        else:
            break
    return can_go_list 

for i in range(4):
    data=input().split()
    for j in range(0,4):
        fish=int(data[j*2])
        dir=int(data[j*2+1]-1)
        
        fishes[i][j]=fish
        directions[i][j]=dir
        heapq.heappush(fishes_q,(fish,i,j))

shark=(0,0)
shark_dir=directions[0][0]

answer=fishes[0][0]
fishes_q.remove((fishes[0][0],0,0))
fishes[0][0]=-1 # 상어

fish_move()

# x,y 로 이동한경우의 총합
def get_total(x,y,dir,total):
    total+=fishes[x][y]
    fishes_q.remove((fishes[x][y],x,y))

    fishes[x][y]=-1
    dir=directions[x][y]
    
    next_list = shark_can_go(x,y,dir)
    maximum,mx,my=0,0,0

    if next_list:
        maximum=0
        for x,y in next_list:
            sub_answer = get_total(x,y,total)
            if sub_answer[0]>maximum:
                mx,my,maximum=x,y,sub_answer[0]


    else:
        return total,x,y

    return maximum,mx,my

while True:
    can_go_list=shark_can_go(shark[0],shark[1],shark_dir)
    if not can_go_list:
        break
    
    maximum=0
    for x,y in can_go_list:
            sub_answer = get_total(x,y,answer)
            maximum=max(maximum,sub_answer)

print(answer)


import sys
import copy
def input(): return sys.stdin.readline().rstrip()

N=4
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# i번 물고기의 좌표를 반환
def find_fish(fishes,i):
    for x in range(N):
        for y in range(N):
            num=fishes[x][y][0]
            if num==i:
                return x,y
    return -1,-1
        
# 모든 물고기 이동
def fish_move(fishes):
    for i in range (1,17):
        x,y=find_fish(fishes,i)

        if x==y==-1:
            continue
        
        dir=fishes[x][y][1]
        for _ in range(8):
            nx,ny= x+dx[dir],y+dy[dir]
            if 0<=nx<N and 0<=ny<N and fishes[nx][ny][0]>=0: # 교체 가능
                fishes[x][y][1]=dir # 회전한 방향으로 재설정
                
                tmp=fishes[x][y]
                fishes[x][y]=fishes[nx][ny]
                fishes[nx][ny]=tmp
                break
            dir=(dir+1)%8

# 상어가 이동할 수 있는 모든 좌표 리스트 반환
def shark_can_go(fishes,x,y,dir):
    can_go_list=[]

    for _ in range(N):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<N and 0<=ny<N and fishes[nx][ny][0]>0:
            can_go_list.append((nx,ny))    
        x,y=nx,ny
    return can_go_list 

# 상어 이동
def shark_move(fishes,x,y,total):
    global maximum
    
    fishes=copy.deepcopy(fishes)
    total+=fishes[x][y][0]
    fishes[x][y][0]=-1

    # 물고기 이동
    fish_move(fishes)

    can_go_list=shark_can_go(fishes,x,y,fishes[x][y][1])
    if len(can_go_list)==0:
        maximum=max(maximum,total)
        return
    
    for next_x, next_y in can_go_list:
        fishes[x][y][0]=0 # 이전칸은 빈칸으로
        shark_move(fishes,next_x,next_y,total)


fishes=[[[0,0]]*4 for _ in range(4)]
maximum=0

for x in range(4):
    data=input().split()
    for y in range(0,4):
        fish=int(data[y*2])
        dir=int(data[y*2+1])-1
        
        fishes[x][y]=[fish,dir]

shark_move(fishes,0,0,0)
print(maximum)
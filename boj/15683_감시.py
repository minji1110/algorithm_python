import sys
def input(): return sys.stdin.readline().rstrip()

direction=[]
room=[]
cctv=[]
n,m=0,0
answer=1e9

def init_direction():
    global direction
    #dx, dy
    up=(-1,0)
    down=(1,0)
    left=(0,-1)
    right=(0,1)
    
    d1=[[up],[down],[left],[right]]
    d2=[[up,down],[left,right]]
    d3=[[up,left],[up,right],[down,left],[down,right]]
    d4=[[up,left,right],[down,left,right],[left,up,down],[right,up,down]]
    d5=[[up,down,left,right]]
    direction=[None,d1,d2,d3,d4,d5]

def init_room():
    global n,m,room
    n,m=map(int,input().split())
    
    for i in range(n):
        room.append(list(map(int,input().split())))
        for j in range(m):
            if 1<=room[i][j]<=5:
                cctv.append((room[i][j],i,j))  #cctv번호, x좌표, y좌표

def update_answer(room):
    global answer
    
    count=0
    for i in range(len(room)):
        count+=room[i].count(0)
    answer=min(answer,count)

def update_room(dir,x,y):
    global room,n,m
    
    for dx,dy in dir:
        nx,ny=x+dx,y+dy
        while(0<=nx<n and 0<=ny<m):
            if room[nx][ny]==6:
                break
            if room[nx][ny]<=0:
                room[nx][ny]-=1
            nx,ny=nx+dx,ny+dy


def reset_room(dir,x,y):
    global room,n,m
    
    for dx,dy in dir:
        nx,ny=x+dx,y+dy
        while(0<=nx<n and 0<=ny<m):
            if room[nx][ny]==6:
                break
            if room[nx][ny]<0:
                room[nx][ny]+=1
            nx,ny=nx+dx,ny+dy

def dfs(index):
    global room
    if index==len(cctv):
        update_answer(room)
        return
    
    cctv_no,x,y = cctv[index]
    for i in range(len(direction[cctv_no])):
        update_room(direction[cctv_no][i],x,y) # 감시
        dfs(index+1)
        reset_room(direction[cctv_no][i],x,y)

init_direction()
init_room()
dfs(0)

print(answer)
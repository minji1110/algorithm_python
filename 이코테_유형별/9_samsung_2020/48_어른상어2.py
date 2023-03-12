import heapq

# 위, 아래, 왼, 오
dx=[None,-1,1,0,0]
dy=[None,0,0,-1,1]
N,M,k=map(int,input().split())

matrix=[]
sharks=[[-1]*3 for _ in range(M+1)] #x, y, 방향
smells=[[[-1]*2 for _ in range(N)] for _ in range(N)] #상어번호, t
dir_info=[[]]

for i in range(N):
    matrix.append(list(map(int,input().split())))
    for j in range(N):
        if matrix[i][j]>0:
            sharks[matrix[i][j]]=[i,j,-1]
            smells[i][j]=[matrix[i][j],k]

dir_input=list(map(int,input().split()))
for i in range(M):
    sharks[i+1][2]=dir_input[i]

for i in range(M):
    dir=[]
    for d in range(4):
        dir.append(list(map(int,input().split())))
    dir_info.append(dir)

def move_sharks():
    for i in range(1,M+1):
        if sharks[i][0]!=-1: # 번호 i 상어 존재
            now_x,now_y,now_dir=sharks[i][0],sharks[i][1],sharks[i][2]
            di=dir_info[i][now_dir-1]

            my_smell=[]
            flag=False

            for d in range(4):
                nx,ny=now_x+dx[di[d]],now_y+dy[di[d]]
                if 0<=nx<N and 0<=ny<N:
                    # 냄새X
                    if smells[nx][ny][0]==-1: 
                        flag=True
                        if matrix[nx][ny]>0: # 이미 상어 존재
                            matrix[now_x][now_y]=0
                            sharks[i]=[-1,-1,-1]
                            break    
                        #이동
                        matrix[now_x][now_y]=0
                        matrix[nx][ny]=i
                        sharks[i]=[nx,ny,di[d]]
                        break
                    
                    elif smells[nx][ny][0]==i:
                        my_smell.append((nx,ny,di[d]))

            if not flag:
                nx,ny,nd=my_smell[0]
                matrix[now_x][now_y]=0
                matrix[nx][ny]=i
                sharks[i]=[nx,ny,nd]


def update_smell():
    for i in range(N):
        for j in range(N):
            if smells[i][j][0]>0:
                smells[i][j][1]-=1
                if smells[i][j][1]==0:
                    smells[i][j]=[-1,-1]
    
    for i in range(1,M+1):
        if sharks[i][0]!=-1:
            x,y=sharks[i][0],sharks[i][1]
            smells[x][y]=[i,k]

def is_end():
    for i in range(2,M+1):
        if sharks[i][0]!=-1:
            return False
    return True

t=0
while True:
    move_sharks()
    update_smell()

    t+=1
    if is_end():
        print(t)
        break
    if t==1000:
        print(-1)
        break
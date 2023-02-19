import sys
def input():return sys.stdin.readline().rstrip()

dx=[None,0,-1,-1,-1,0,1,1,1]
dy=[None,-1,-1,0,1,1,1,0,-1]

N,M=map(int,input().split())
matrix=[]
move=[]
clouds= [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 구름 이동
def move_clouds(d,s):
    move_cnt=s%N
    for i in range(len(clouds)):
        cx,cy=clouds[i]
        nx,ny = (cx+(move_cnt*dx[d]))%(N) , (cy+(move_cnt*dy[d]))%(N)
        clouds[i]=(nx,ny)
        clouds[nx][ny]+=1

# 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
def water_copy_bug(r,c):
    diag_x=[-1,-1,1,1]
    diag_y=[-1,1,-1,1]
    
    amount=0
    for i in range(4):
        nx,ny=r+diag_x[i],c+diag_y[i]
        if 0<=nx<N and 0<=ny<N and matrix[nx][ny]>0:
            amount+=1
    matrix[r][c]+=amount

def make_clouds(clouds):
    new_clouds=[]
    for x in range(N):
        for y in range(N):
            if matrix[x][y]>=2:
                # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
                if (x,y) not in clouds:
                    matrix[x][y]-=2
                    new_clouds.append((x,y))
    return new_clouds
    
for _ in range(N):
    matrix.append(list(map(int,input().split())))

for _ in range(M):
    d,s=map(int,input().split())
    move.append((d,s))

for d,s in move:
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    # 2.각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    move_clouds(d,s)
   
    # 3. 구름이 모두 사라진다.
    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 
    for r,c in clouds:
        water_copy_bug(r,c)

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    clouds=make_clouds(clouds)

answer=0
for i in range(len(matrix)):
    answer+=sum(matrix[i])
print(answer)
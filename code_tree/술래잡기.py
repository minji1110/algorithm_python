# d가 1인 경우 좌우로 움직임을, 2인 경우 상하로만 움직임
# 상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,h,k=map(int,input().split())
matrix=[[[] for _ in range(n)] for _ in range(n)]

clockwise_path=[]
anti_clockwise_path=[]

def init_paths():
    for i in range(1, n):
        di_list = [[2, 3], [0, 1]]
        for di in di_list[i % 2]:
            for j in range(1, i + 1):
                look_at = di if j != i else (di + 1) % 4
                clockwise_path.append((di, look_at))
    for i in range(1, n):
        clockwise_path.append((0, 0))
    clockwise_path[-1]=(0,2)

    for i in range(1, n - 1):
        anti_clockwise_path.append((2, 2))
    anti_clockwise_path.append((2, 1))

    for i in range(n - 1, 0, -1):
        di_list = [[1, 0], [3, 2]]
        for di in di_list[i % 2]:
            for j in range(1, i + 1):
                look_at = di if j != i else (di - 1) % 4
                anti_clockwise_path.append((di, look_at))
    anti_clockwise_path[-1]=(2,0)

init_paths()
cx,cy=n//2,n//2 #술래 위치
c_dir,c_look=0,0
path=clockwise_path
path_index=0

runners=[]
for _ in range(m):
    runner_x,runner_y,runner_dir=map(int,input().split())
    runners.append((runner_x-1,runner_y-1,runner_dir))
    matrix[runner_x-1][runner_y-1].append(runner_dir)

trees=[[False]*n for _ in range(n)]
for _ in range(h):
    tx,ty=map(int,input().split())
    trees[tx-1][ty-1]=True

def runner_move():
    new_runners=[]

    for i in range(len(runners)):
        rx, ry, r_dir=runners[i]
        if abs(cx-rx)+abs(cy-ry)<=3: # 현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
            n_dir=r_dir
            nx,ny=rx+dx[n_dir],ry+dy[n_dir]
            if not (0<=nx<n and 0<=ny<n): # 범위 벗어날 경우 방향 전환
                n_dir = (r_dir + 2) % 4
                nx, ny = rx + dx[n_dir], ry + dy[n_dir]
            if nx==cx and ny==cy:
                nx,ny=rx,ry

            new_runners.append((nx,ny,n_dir))
            runners[i]=(nx,ny,n_dir)
            matrix[rx][ry].remove(r_dir)

    for rx,ry, r_dir in new_runners:
        matrix[rx][ry].append(r_dir)

def catcher_move():
    global cx,cy,c_dir,c_look,path_index,answer,turn

    c_dir,c_look=path[path_index]
    cx,cy=cx+dx[c_dir],cy+dy[c_dir]

    catch_count=0
    for c in range(0,3):
        check_x,check_y=cx+c*dx[c_look], cy+c*dy[c_look]
        if not (0<=check_x<n and 0<=check_y<n):
            break
        if trees[check_x][check_y]:

            continue
        if matrix[check_x][check_y]:
            catch_count+=len(matrix[check_x][check_y])
            for rd in matrix[check_x][check_y]:
                runners.remove((check_x,check_y,rd))
            matrix[check_x][check_y]=[]
    answer+=turn*catch_count
    path_index+=1

turn=1
answer=0

def print_matrix():
    for i in range(n):
        print(matrix[i])

while turn<=k:
    runner_move()
    catcher_move()

    if not runners:
        break
    if cx==0 and cy==0:
        path=anti_clockwise_path
        path_index=0
    if cx==n//2 and cy==n//2:
        path=clockwise_path
        path_index = 0
    turn+=1

print(answer)

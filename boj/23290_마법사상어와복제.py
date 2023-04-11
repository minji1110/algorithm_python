N=4
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]
shark_move_order=[]

def can_go(x,y):
    return 0<=x<N and 0<=y<N and not (x==sx and y==sy) and not smells[x][y]

def move_all_fishes():
    global fishes
    new_fishes=[[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if fishes[i][j]:  # 물고기 있는 칸이면 모든 물고기 이동
                for fd in fishes[i][j]:
                    ni, nj, nd = i, j, fd
                    for _ in range(8):
                        ni, nj = i + dx[nd], j + dy[nd]
                        if can_go(ni, nj):
                            new_fishes[ni][nj].append(nd)
                            nd=-1
                            break
                        nd = (nd - 1) % 8
                    if nd==fd: # 이동 불가
                        new_fishes[i][j].append(fd)
    fishes=new_fishes

def move_shark():
    global sx,sy
    max_fish_count=-1
    selected_order=[]

    for order in shark_move_order:
        valid=True
        visited = []
        nx,ny=sx,sy
        fish_count=0
        for o in order:
            nx,ny=nx+dx[o],ny+dy[o]
            if not (0<=nx<N and 0<=ny<N):
                valid=False
                break
            if fishes[nx][ny]:
                if (nx,ny) not in visited:
                    fish_count+=len(fishes[nx][ny])
                visited.append((nx,ny))

        if valid and fish_count>max_fish_count: # 3칸 연속 이동 가능
            max_fish_count=fish_count
            selected_order=order

    for o in selected_order: # 이동
        sx,sy=sx+dx[o],sy+dy[o]
        if fishes[sx][sy]:
            for sml in range(len(fishes)):
                smells[sx][sy].append(step)
            fishes[sx][sy]=[]

def refresh_smells():
    for i in range(N):
        for j in range(N):
            if smells[i][j] and smells[i][j][0]==step-2:
                rmv_index=0
                for _ in range(len(smells[i][j])):
                    if smells[i][j][rmv_index]!=step-2:
                        break
                    rmv_index+=1
                smells[i][j]=smells[i][j][rmv_index:]

def make_shark_move_order():
    # 상,좌,하,우
    dirs=[2,0,6,4]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                shark_move_order.append([dirs[i],dirs[j],dirs[k]])

def get_answer():
    count=0
    for i in range(N):
        for j in range(N):
            count+=len(fishes[i][j])
    return count

make_shark_move_order()
for tc in range(1):
    # tc_num=int(input())

    fishes=[[[] for _ in range(N)] for _ in range(N)]
    smells=[[[] for _ in range(N)] for _ in range(N)]

    M,S=map(int,input().split())
    for _ in range(M):
        fx,fy,d=map(int,input().split())
        fishes[fx-1][fy-1].append(d-1)

    sx,sy=map(int,input().split())
    sx,sy=sx-1,sy-1

    step=1
    while True:
        if step>S:
            break
        # 1. 복제 마법 실행
        dup_fishes=[f[:] for f in fishes[:]]

        # 2. 물고기 한 칸 이동
        move_all_fishes()

        # 3. 상어 이동
        move_shark()

        # 4. 두번 전 냄새 사라짐
        refresh_smells()

        # 5. 복제 마법 완료
        for i in range(N):
            for j in range(N):
                if dup_fishes[i][j]:
                    for dfd in dup_fishes[i][j]:
                        fishes[i][j].append(dfd)
        step += 1

    answer=get_answer()
    print(answer)

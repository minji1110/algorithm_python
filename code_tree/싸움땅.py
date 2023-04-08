# 상,우,하,좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, k = map(int, input().split())
gun_matrix = [] # 해당 칸의 총들의 공격력, 총 없는경우 빈 리스트
players_matrix =[[-1]*n for _ in range(n)] # 해당 칸의 플레이어 번호
players_info = [] # 플레이어 정보

def init_gun_matrix():
    for _ in range(n):
        gun_matrix.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            gun_power = gun_matrix[i][j]
            gun_matrix[i][j] = [gun_power] if gun_power>0 else []

def init_players():
    for no in range(m):
        x, y, d, s = map(int, input().split())
        players_info.append([x-1,y-1,d, s, 0])  # x,y,방향,초기능력치,총의공격력
        players_matrix[x-1][y-1]=no

def win(pno,point):
    points[pno]+=point
    x, y, d, s, gp = players_info[pno]
    players_matrix[x][y]=pno

    if gun_matrix[x][y]:
        max_power=max(gun_matrix[x][y])
        if gp<max_power:
            players_info[pno][4]=max_power
            gun_matrix[x][y].remove(max_power)
            if gp>0:
                gun_matrix[x][y].append(gp)

def lose(pno):
    x, y, d, s, gp = players_info[pno]
    if gp>0:
        gun_matrix[x][y].append(gp)
    players_info[pno][4]=0

    nx,ny=x+dx[d],y+dy[d]
    for _ in range(4):
        if not (0 <= nx < n and 0 <= ny < n) or players_matrix[nx][ny]!=-1:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]
        else:
            break

    players_info[pno][0],players_info[pno][1],players_info[pno][2]=nx,ny,d
    players_matrix[nx][ny]=pno

    if gun_matrix[nx][ny]:
        max_power=max(gun_matrix[nx][ny])
        players_info[pno][4]=max_power
        gun_matrix[nx][ny].remove(max_power)

def fight(pno1, pno2): # pno1번, pno2번 플레이어 싸움
    x1,y1,d1,s1,pgp1=players_info[pno1]
    x2,y2,d2,s2,pgp2=players_info[pno2]

    if abs((s1+pgp1)-(s2+pgp2))>0:
        if (s1+pgp1)>(s2+pgp2):
            lose(pno2)
            win(pno1,abs((s1+pgp1)-(s2+pgp2)))
        else:
            lose(pno1)
            win(pno2,abs((s1+pgp1)-(s2+pgp2)))
    else:
        if s1>s2:
            lose(pno2)
            win(pno1,0)
        else:
            lose(pno1)
            win(pno2,0)

def move_all_players():
    for pno in range(m):
        px, py, pd, ps, pgp = players_info[pno]

        # 다음 px,py,pd 결정
        nx,ny,nd =px + dx[pd],py + dy[pd], pd
        if not (0 <= nx < n and 0<=ny < n):
            nd = (pd + 2) % 4
            nx,ny=px+dx[nd],py+dy[nd]

        players_info[pno][0],players_info[pno][1],players_info[pno][2]=nx,ny,nd
        players_matrix[px][py] = -1  # 자리 비우기

        #이동
        if players_matrix[nx][ny]==-1: # 플레이어 없는 경우
            # 총 있는 경우
            if gun_matrix[nx][ny]:
                maximum_power=max(gun_matrix[nx][ny])
                if maximum_power>pgp:
                    if pgp>0:
                        gun_matrix[nx][ny].append(pgp)
                    gun_matrix[nx][ny].remove(maximum_power)
                    players_info[pno][4]=maximum_power
            players_matrix[nx][ny]=pno

        else: # 플레이어 있는 경우
            fight(pno,players_matrix[nx][ny])

init_gun_matrix()
init_players()

points = [0] * m
for _ in range(k):
    move_all_players()

for pt in points:
    print(pt,end=' ')

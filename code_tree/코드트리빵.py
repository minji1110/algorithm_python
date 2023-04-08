from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
matrix = []
base_camps = []
stores = [(-1, -1)]
people_in_matrix = []  # (번호, x, y)
shortest_path = [[] for _ in range(m+1)]

def init_data():
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        for j in range(n):
            if matrix[i][j] == 1:
                base_camps.append((i, j))
    for i in range(m):
        stx, sty = map(int, input().split())
        stores.append((stx - 1, sty - 1))

def select_basecamp(no):  # 출발할 베이스캠프를 선택
    store_x, store_y = stores[no]
    min_bx, min_by, min_dist = -1, -1, n * n

    for bx, by in base_camps:
        q = deque()
        visited = [[False] * n for _ in range(n)]
        q.append((0, bx, by))
        visited[bx][by] = True

        while q:
            dist, x, y = q.popleft()
            if x == store_x and y == store_y:
                if min_dist > dist:
                    min_bx, min_by, min_dist = bx, by, dist
                break
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] >= 0:
                    q.append((dist + 1, nx, ny))
                    visited[nx][ny] = True
    return min_bx, min_by

def get_shortest_path(no,sx,sy):
    store_x, store_y = stores[no]

    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((sx, sy, deque([(sx,sy)])))
    visited[sx][sy] = True

    while q:
        x,y,trace= q.popleft()
        if x == store_x and y == store_y:
            trace.popleft() # 출발점 제거
            return trace

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] >= 0:
                tmp_trace=deque(list(trace)[:])
                tmp_trace.append((nx,ny))
                q.append((nx, ny,tmp_trace))
                visited[nx][ny] = True

def update_shortest_path(blocked_x, blocked_y): # x,y 를 지날 수 없게된 경우 업데이트
    for pno,px,py in people_in_matrix:
        if (blocked_x, blocked_y) in shortest_path[pno]:
            shortest_path[pno]=get_shortest_path(pno,px,py)

def start(no):  # no번 사람 출발
    bx, by = select_basecamp(no)
    base_camps.remove((bx, by))
    matrix[bx][by] = -1
    update_shortest_path(bx, by)

    people_in_matrix.append((no, bx, by))
    shortest_path[no] = get_shortest_path(no,bx,by)

def move_all_people(): # 모든 사람 이동
    for p in range(len(people_in_matrix)):
        pno, px, py = people_in_matrix[p]
        nx, ny = shortest_path[pno].popleft()
        people_in_matrix[p]= (pno,nx,ny)

def check_arrived_people():
    global rest_people

    need_to_remove = []
    for no,x,y in people_in_matrix:
        if x==stores[no][0] and y==stores[no][1]:
            need_to_remove.append((no,x,y))
            matrix[x][y]=-1
            rest_people-=1
    for rno,rx,ry in need_to_remove:
        people_in_matrix.remove((rno,rx,ry))
        update_shortest_path(rx,ry)

init_data()
t = 0
rest_people = m
while rest_people>0:
    t += 1
    # 1. 모든 사람이 최단거리로 이동
    move_all_people()

    # 2. 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고, 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
    check_arrived_people()

    # 3. t번째 사람 출발
    if t <= m:
        start(t)
print(t)

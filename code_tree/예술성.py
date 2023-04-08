from collections import deque
N=int(input())
matrix=[]
for _ in range(N):
    matrix.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 조화로움 점수를 계산
def calculate(group_info,adj_count):
    # group_info : 숫자 값, 그룹 크기
    result=0
    total_groups=len(group_info)
    for i in range(0,total_groups-1):
        for j in range(i+1,total_groups):
            if adj_count[i][j]>0:
                result+=(group_info[i][1]+group_info[j][1])*group_info[i][0]*group_info[j][0]*adj_count[i][j]
    return result

# 모든 그룹에 대해, 두 그룹이 겹치는 변의 수를 구함
def get_adjacent_count(total_group_num,group_matrix): # 그룹 수, 격자 정보
    result=[[0]*total_group_num for _ in range(total_group_num)]
    q=deque()
    visited = [[False] * N for _ in range(N)]

    q.append((0,0))
    visited[0][0]=True

    while q:
        x,y=q.popleft()
        g_number=group_matrix[x][y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if group_matrix[nx][ny]!=g_number:
                    result[g_number][group_matrix[nx][ny]]+=1
                if not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=True
    return result

def get_score():
    q=deque()
    visited=[[False]*N for _ in range(N)]
    group_number=0 # 그룹 번호 0번부터
    group_matrix=[[-1]*N for _ in range(N)] # 각 위치의 그룹 번호
    group_info=[] # 각 그룹의 숫자, 크기

    # group_matrix 에 해당 그룹 번호를 세팅
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                group_len=0
                q.append((i,j))
                visited[i][j]=True
                group_matrix[i][j]=group_number

                while q:
                    x,y=q.popleft()
                    group_len+=1
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<N and 0<=ny<N:
                            if not visited[nx][ny] and matrix[nx][ny]==matrix[x][y]:
                                q.append((nx,ny))
                                visited[nx][ny]=True
                                group_matrix[nx][ny]=group_number

                group_info.append((matrix[i][j],group_len))
                group_number+=1

    adj_count=get_adjacent_count(len(group_info),group_matrix)
    score=calculate(group_info,adj_count)
    return score

def rotate_matrix():
    global matrix
    new_matrix = [[0] * N for _ in range(N)]
    # 십자 회전
    for i in range(N):
        new_matrix[i][N//2],new_matrix[N//2][i]=matrix[N//2][N-1-i],matrix[i][N//2]
    # 나머지 회전
    grid_len=(N-1)//2 #한 변 길이
    for row in range(0,N,grid_len+1):
        for col in range(0,N,grid_len+1):
            for i in range(grid_len):
                for j in range(grid_len):
                    new_matrix[row+j][col+grid_len-1-i]=matrix[row+i][col+j]
    matrix=new_matrix

answer=0
for repeat in range(4):
    answer+=get_score()
    if repeat==3:
        break
    rotate_matrix()
print(answer)

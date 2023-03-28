N,Q=map(int,input().split())
matrix=[]
for _ in range(2**N):
    matrix.append(list(map(int,input().split())))
L_list=list(map(int,input().split()))
len_of_grids=2**(N-L_list[0])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#배열을 회전시키는 함수 : seperate_grid()보다 빠름! 슬라이싱대신 직접 회전할것!!
def rotate2():
    global matrix
    new_matrix=[m[:] for m in matrix[:]]

    #i,j를 기준으로 2**l크기의 배열만 회전시킴
    for i in range(0, 2**N, 2**L):
        for j in range(0, 2 ** N, 2**L):
            for k in range(2**L):
                for m in range(2**L):
                    new_matrix[i+k][j+m] = matrix[i + (2**L - 1 - m)][j + k]

    matrix=new_matrix

#격자를 90도 회전한다.
def rotate_grid(i,j):
    grid=[m[j:j+len_of_grids] for m in matrix[i:i+len_of_grids][::-1]]
    grid=list(map(list,zip(*grid)))

    for k in range(0,len_of_grids):
        matrix[i+k][j:j+len_of_grids]=grid[k]

#격자를 2L × 2L 크기의 부분 격자로 나눈다. 
def seperate_grid():
    i=0
    while True:
        j=0
        while True:
            rotate_grid(i,j) #회전
            j+=len_of_grids
            if j>=2**N:
                break

        i+=len_of_grids
        if i>=2**N:
            break

#얼음 양을 감소한다.
def reduce_ice():
    global matrix
    new_matrix=[m[:] for m in matrix[:]]
    
    #얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    for i in range(2**N):
        for j in range(2**N):
            if matrix[i][j]>0:
                not_valid=0
                for d in range(4):
                    nx,ny=i+dx[d],j+dy[d]
                    if not (0<=nx<2**N and 0<=ny<2**N):
                        not_valid+=1
                    else:
                        if matrix[nx][ny]==0:
                            not_valid+=1
                    if not_valid>1:
                        new_matrix[i][j]=matrix[i][j]-1
                        break
    matrix=new_matrix

# 남아있는 얼음의 합, 가장 큰 덩어리의 개수 출력
from collections import deque
def print_answer():
    total_amount=0
    maximum_count=0
    visited=[[False]*2**N for _ in range(2**N)]

    for i in range(2**N):
        for j in range(2**N):
            total_amount+=matrix[i][j]
            if not visited[i][j] and matrix[i][j]>0:
                count=0
                q=deque()
                q.append((i,j))
                visited[i][j]=True

                while q:
                    x,y=q.popleft()
                    count+=1
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<2**N and 0<=ny<2**N and not visited[nx][ny]:
                            if matrix[nx][ny]>0:
                                q.append((nx,ny))
                                visited[nx][ny]=True

                if count>maximum_count:
                    maximum_count=count
    
    print(total_amount)
    print(maximum_count)

# main
for L in L_list:
    len_of_grids=2**L
    rotate2()
    # seperate_grid()
    reduce_ice()

print_answer()
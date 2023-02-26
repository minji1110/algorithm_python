from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 2차원 배열을 90도 회전
def rotate_matrix(matrix):
    n=len(matrix)
    result=[[0]*n for _ in range(n)]
    for row in range(n):
        for column in range(n):
            result[column][n-1-row]=matrix[row][column]
    return result

# n개의 블럭으로 이루어진 정보 리스트
def make_block_list(table):
    n=len(table)
    block_list=[[] for _ in range(7)]
    visited=[[False]*n for _ in range(n)]
    
    q=deque()
    for i in range(n):
        for j in range(n):
            if table[i][j]==1 and not visited[i][j]: # 블럭이 놓임
                block_info=[]
                cnt=0
                
                sx,sy=i,j
                q.append((i,j))
                visited[i][j]=True
                cnt+=1

                while q:
                    x,y=q.popleft()
                    block_info.append((x-sx,y-sy)) # 상대 좌표 저장
                    
                    for d in range(4):
                        nx,ny=x+dx[d],y+dy[d]
                        if 0<=nx<n and 0<=ny<n and table[nx][ny]==1 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
                            cnt+=1
                block_list[cnt].append((block_info)) # 사용여부, 좌표정보
    
    return block_list

def solution(game_board, table):
    answer = 0
    n=len(game_board)    

    block_list=make_block_list(table)
    visited=[[False]*n for _ in range(n)]
    q=deque()

    # 4번의 회전에 대해 검사
    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if game_board[i][j]==0 and not visited[i][j]:
                    tmp_visited=[]
                    board_info=[]
                    cnt=0
                    sx,sy=i,j

                    q.append((i,j))
                    visited[i][j]=True
                    cnt+=1

                    while q:
                        x,y=q.popleft()
                        board_info.append((x-sx,y-sy))
                        tmp_visited.append((x,y))

                        for d in range(4):
                            nx,ny=x+dx[d],y+dy[d]
                            if 0<=nx<n and 0<=ny<n and game_board[nx][ny]==0 and not visited[nx][ny]:
                                q.append((nx,ny))
                                visited[nx][ny]=True
                                cnt+=1

                    matched=False
                    for block_info in block_list[cnt]: # 개수가 맞는 블럭들에 대해
                        if block_info==board_info:
                            matched=True
                            block_list[cnt].remove(block_info)
                            answer+=cnt
                            break
                    
                    if not matched:
                        for vx,vy in tmp_visited:
                            visited[vx][vy]=False

        game_board=rotate_matrix(game_board)
        visited=rotate_matrix(visited)
    return answer

game_board=[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table=[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

game_board=[[0,1,1],[1,0,1],[1,1,0]]
table=[[1,0,1],[0,0,0],[1,0,1]]
print(solution(game_board,table))
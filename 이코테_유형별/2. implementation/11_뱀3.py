import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

N=int(input())
K=int(input())
board=[[0]*N for _ in range(N)] # 1 사과 2 뱀

for _ in range(K):
    x,y=map(int,input().split())
    board[x-1][y-1]=1

L=int(input())
turn_q=deque()

for _ in range(L):
    turn_t,turn_dir=input().split()
    turn_q.append((int(turn_t),turn_dir))

# 동, 북, 서, 남 (왼 +1 오 -1)
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def turn(turn_dir):
    if turn_dir=='L':
        return (now_dir+1)%4
    else:
        return (now_dir-1)%4

#초기설정
t=0
board[0][0]=2
now_x,now_y,now_dir=0,0,0
next_turn_t, next_turn_dir=turn_q.popleft()
snake_q=deque()
snake_q.append((now_x,now_y))

while True:
    t+=1
    nx,ny=now_x+dx[now_dir], now_y+dy[now_dir]
    
    # 범위 벗어남
    if not(0<=nx<N and 0<=ny<N):
        break
    # 자기 몸 존재
    if board[nx][ny]==2:
        break

    if board[nx][ny]==0:
        pop_x,pop_y=snake_q.popleft()
        board[pop_x][pop_y]=0
    # 사과
    elif board[nx][ny]==1:
        board[nx][ny]=0
    
    snake_q.append((nx,ny))
    board[nx][ny]=2
    now_x,now_y=nx,ny

    if t==next_turn_t:
        now_dir= turn(next_turn_dir)
        if turn_q:
            next_turn_t,next_turn_dir=turn_q.popleft()

print(t)
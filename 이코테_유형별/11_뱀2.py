import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

'''
 동, 북, 서, 남
 왼 회전시 +1, 오 회전시 -1
'''
dx=[0,-1,0,1]
dy=[1,0,-1,0]

# 회전 처리
def turn(dir, turn_dir):
    #왼 회전
    if turn_dir=='L': 
        if dir==3:
            return 0
        else :
            return dir+1
    #오 회전
    else:
        if dir==0:
            return 3
        else:
            return dir-1


N=int(input())
board=[[0] *(N+1) for _ in range(N+1)]

K=int(input())
for _ in range(K):
    x,y=map(int,input().split())
    board[x][y]=-1

L=int(input())
turn_q=deque()
for _ in range(L):
    t,dir=input().split()
    turn_q.append((int(t),dir))

times=0
dir=0 # 동쪽
x,y=1,1 #머리 좌표
move_q=deque()
board[x][y]=1 # 뱀 놓인자리 1, 빈자리 0, 사과 -1

move_q.append((x,y))
turn_t,turn_dir=turn_q.popleft()

while True:
    # 1초에 1while
    times+=1
    x,y = x+dx[dir],y+dy[dir]

    if not (1<=x<=N and 1<=y<=N) : # 범위 out
        break
    else:
        # 사과 : 머리만 전진
        if board[x][y]==-1: 
            board[x][y]=1
            move_q.append((x,y))
        # 사과x : 머리, 꼬리 전진
        elif board[x][y]==0: 
            board[x][y]=1
            move_q.append((x,y))
            
            pop_x,pop_y=move_q.popleft()
            board[pop_x][pop_y]=0

        # 몸 부딪힘
        else:
            break

    # times 초 끝, turn 확인
    if times==turn_t:
        dir=turn(dir,turn_dir)
        if turn_q:
            turn_t,turn_dir=turn_q.popleft()
    
print(times)


# 대차게 실패.. 다시풀기
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

n=int(input())
board=[[0 for _ in range(n+1)] for _ in range(n+1)]

apples=int(input())
for a in range(apples):
    x,y=map(int,input().split())
    board[x][y]=-1

turns=int(input())
turn_q = deque()
for turn in range(turns):
    time, direction = input().split()
    time=int(time)
    
    turn_q.append((time,direction))

bl=1 #몸길이

look_at=0 # 0(오),1(왼),2(상),3(하)
next_look_at=[[3,2],[2,3],[0,1],[1,0]]

x=1
y=1
tail_x=1
tail_y=1

def locate_head():
    if look_at==0: #오
        head=(x,y+1)
    elif look_at==1: #왼
        head=(x,y-1)
    elif look_at==2: #상
        head=(x-1,y)
    else: #하
        head=(x+1,y)
    print('head=',head)
    return head

def locate_tail():
    if look_at==0: #오
        tail=(x,y+1-bl)
    elif look_at==1: #왼
        tail=(x,y-1+bl)
    elif look_at==2: #상
        tail=(x-1+bl,y)
    else: #하
        tail=(x+1-bl,y)
    print('tail=',tail)
    return tail

def turn():
    print('turn!')
    if turn_q:
        next, dir = turn_q.popleft()
        return next,dir
    else:
        return -1,'X'

def is_head_valid(head_x,head_y):
    return 1<=head_x<=n and 1<=head_y<=n

def is_tail_valid(tail_x,tail_y):
    return  1<=tail_x<=n and 1<= tail_y<=n

times=0
next_turn_t, next_turn_dir=turn_q.popleft()

while(True):
    times+=1
    # 머리 이동
    x,y=locate_head()
    if not is_head_valid(x,y):
        break

    # 사과 있는가?
    if board[x][y]==-1:
        bl+=1

    #꼬리 이동   
    else:
        tail_x,tail_y=locate_tail() 
    if not is_tail_valid(tail_x,tail_y):
        break
    
    #turn!
    if next_turn_t==times:
        if next_turn_dir=='D':
            look_at=next_look_at[look_at][0]
        else:
            look_at=next_look_at[look_at][1]
        next_turn_t,next_turn_dir=turn()
        locate_tail()
        if not is_tail_valid(tail_x,tail_y):
            break

print(times)


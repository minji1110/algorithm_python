import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

N,K=map(int,input().split())
durability=list(map(int,input().split()))

durability=deque(durability)
robots=deque([-1]*(2*N))

START=0 # 올리는 위치
END=N-1 # 내리는 위치

step=0
while True:
    step+=1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    durability.rotate(1)
    robots.rotate(1)
    
    # 도착한 로봇 내리기
    robots[END]=-1

    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    #2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(END-1,-1,-1):
        if robots[i]==1: # 로봇이 있는 경우
            next=i+1
            if robots[next]==-1 and durability[next]>=1:
                robots[next]=1
                durability[next]-=1
                robots[i]=-1

                robots[END]=-1


    #3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if durability[START]!=0:
        robots[START]=1
        durability[START]-=1
    
    #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if durability.count(0)>=K:
        break

print(step)
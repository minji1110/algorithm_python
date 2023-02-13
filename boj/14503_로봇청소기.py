import sys
def input(): return sys.stdin.readline().rstrip()

#북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

N,M=map(int,input().split())
now_x,now_y,now_dir=map(int,input().split())
room=[]
for _ in range(N):
    room.append(list(map(int,input().split())))

answer=0
while True:
    if room[now_x][now_y]==0:
        room[now_x][now_y]=2
        answer+=1
    else:
        can_go=False
        for _ in range(4):
            # 반시계 방향으로 회전한다.
            now_dir=(now_dir-1)%4 
            
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            nx,ny=now_x+dx[now_dir],now_y+dy[now_dir]
            if room[nx][ny]==0:
                can_go=True
                now_x,now_y=nx,ny
                break
        if not can_go:
            #바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            b_dir=(now_dir+2)%4
            bx,by=now_x+dx[b_dir],now_y+dy[b_dir]
            if room[bx][by]!=1:
                now_x,now_y=bx,by
                continue
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
print(answer)
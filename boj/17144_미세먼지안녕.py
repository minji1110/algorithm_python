import sys
def input() : return sys.stdin.readline().rstrip()

R,C,T = map(int,input().split())
house=[]
cleaner_upper,cleaner_lower=-1,-1 # 공기청정기 위쪽, 아래쪽의 x좌표
for r in range(R):
    house.append(list(map(int,input().split())))
    for c in range(C):
        if house[r][c]==-1:
            if cleaner_upper==-1:
                cleaner_upper=r
            else:
                cleaner_lower=r

#미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
def spread_dust():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    tmp_dust=[[0]*C for _ in range(R)]
    
    # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    for r in range(R):
        for c in range(C):
            if house[r][c]!=-1:
                spread_cnt=0
                spread_amount=house[r][c]//5 # 확산되는 양은 Ar,c/5이고 소수점은 버린다.
                for d in range(4):
                    nr,nc=r+dx[d],c+dy[d]
                    # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                    if not (0<=nr<R and 0<=nc<C) or house[nr][nc]==-1:
                        continue
                    spread_cnt+=1
                    tmp_dust[nr][nc]+=spread_amount
                house[r][c]-=(spread_amount*spread_cnt) # (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.

    for r in range(R):
        for c in range(C):
            if house[r][c]!=-1:
                house[r][c]+=tmp_dust[r][c]

def work_cleaner():
    # 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 
    prev=house[cleaner_upper][1]
    house[cleaner_upper][1]=0
    for i in range(2,C): # 오
        tmp=house[cleaner_upper][i]
        house[cleaner_upper][i]=prev
        prev=tmp
    
    for i in range(cleaner_upper-1,-1,-1): # 위
        tmp=house[i][C-1]
        house[i][C-1]=prev
        prev=tmp
    
    for i in range(C-2,-1,-1): # 왼
        tmp=house[0][i]
        house[0][i]=prev
        prev=tmp
    
    for i in range(1,cleaner_upper): # 아래
        tmp=house[i][0]
        house[i][0]=prev
        prev=tmp    
    
    # 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    prev=house[cleaner_lower][1]
    house[cleaner_lower][1]=0

    for i in range(2,C): # 오
        tmp=house[cleaner_lower][i]
        house[cleaner_lower][i]=prev
        prev=tmp
        
    for i in range(cleaner_lower+1,R): # 아래
        tmp=house[i][C-1]
        house[i][C-1]=prev
        prev=tmp 
        
    for i in range(C-2,-1,-1): # 왼
        tmp=house[R-1][i]
        house[R-1][i]=prev
        prev=tmp
        
    for i in range(R-2,cleaner_lower,-1): # 위
        tmp=house[i][0]
        house[i][0]=prev
        prev=tmp

while T>0:
    spread_dust()
    work_cleaner()   
    T-=1

answer=0
for r in range(R):
    answer+=sum(house[r])
print(answer+2)
import sys
def input() : return sys.stdin.readline().rstrip()

# 왼위, 왼, 왼아래
dx=[-1,0,1]
dy=[-1,-1,-1]

def set_golds(golds):
    for j in range(1,m+1):
        for i in range(1,n+1):
            tmp=golds[i][j]
            for k in range(3):
                nx,ny=i+dx[k],j+dy[k]
                golds[i][j]=max(golds[i][j],tmp+golds[nx][ny])

test_case = int(input())
for _ in range(test_case):
    n,m=map(int,input().split())
    golds=[[0]*(m+1) for _ in range(n+2)]
    
    data=list(map(int,input().split()))
    for i in range(n):
        for j in range(m):
            golds[i+1]=[0]+data[i*m : i*m + m]
    
    set_golds(golds)
    
    maximum=0
    for i in range(len(golds)):
        maximum=max(maximum,golds[i][-1])
    print(maximum)
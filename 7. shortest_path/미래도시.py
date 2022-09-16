import sys
INF = int(1e9)
def input() : return sys.stdin.readline().rstrip()

n, m = map(int, input().split())    # 회사의 수, 경로의 수
matrix=[[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    matrix[i][i]=0

for _ in  range(m):
    v1, v2 = map(int , input().split())
    matrix[v1][v2]=matrix[v2][v1]=1

dest2, dest1 = map(int, input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            matrix[a][b]=min(matrix[a][b],matrix[a][k]+matrix[k][b])

distance1=matrix[1][dest1]
distance2=matrix[dest1][dest2]
if(distance1==INF or distance2==INF): print(-1)
else: print(distance1+distance2)
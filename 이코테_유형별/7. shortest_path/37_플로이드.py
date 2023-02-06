import sys
def input(): return sys.stdin.readline().rstrip()
INF=1e9

node=int(input())
edge=int(input())
matrix = [[INF] * (node+1) for _ in range(node+1)]
for i in range(node+1):
    matrix[i][i]=0

for _ in range(edge):
    a,b,cost=map(int,input().split())
    matrix[a][b]=min(matrix[a][b],cost)

for k in range(1,node+1):
    for a in range(1,node+1):
        for b in range(1,node+1):
            matrix[a][b]=min(matrix[a][b], matrix[a][k]+matrix[k][b])

for i in range(1,node+1):
    for j in range(1, node+1):
        if matrix[i][j]==INF:
            matrix[i][j]=0
        print(matrix[i][j], end=" ")
    print()


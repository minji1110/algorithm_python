# 이코테 5-10 . 음료수 얼려먹기
from collections import deque

# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(matrix, x, y):
    matrix[x][y]=2
    for i in range(4):
        nextX,nextY=x+dx[i],y+dy[i]
        if 0<=nextX<len(matrix) and 0<= nextY < len(matrix[0]) and matrix[nextX][nextY]==0:
            dfs(matrix,nextX, nextY)

n,m=map(int, input().split())
matrix=[]

for i in range(n):
    matrix.append(list(map(int, input())))

cnt=0
for x in range (n):
    for y in range (m):
        if matrix[x][y]==0:
            cnt+=1
            dfs(matrix,x,y)

print(cnt)
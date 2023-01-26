import sys
# import common
import heapq
  
def get_line(): 
    return sys.stdin.readline().rstrip()

def get_ints():
    return map(int,get_line().split())

def print_array(array):
    for i in range(len(array)):
            print(array[i])
'''
N*N 시험관
1~K 번 종류의 바이러스
낮은 번호부터 증식
S 초 지난 후 (x,y) 의 바이러스는?
'''

matrix=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,k = get_ints()
for _ in range(n):
    matrix.append(list(map(int,get_line().split())))
s,X,Y = get_ints()

pq=[]
for i in range(n):
    for j in range(n):
        if matrix[i][j]>0:
            virus=matrix[i][j]
            heapq.heappush(pq,(0,virus,i,j))

while pq:
    t,virus,x,y=heapq.heappop(pq)
    if t==s:
        break

    for i in range(0,4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and matrix[nx][ny]==0:
            matrix[nx][ny]=virus
            heapq.heappush(pq,(t+1,virus,nx,ny))

print(matrix[X-1][Y-1])


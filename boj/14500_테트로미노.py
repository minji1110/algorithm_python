import sys
def input(): return sys.stdin.readline().rstrip()

matrix=[]
N,M=map(int,input().split())
for _ in range(N):
    matrix.append(list(map(int,input().split())))

#2*3 에 놓을 수 있는 모양들. 6칸중 뺄 2칸의 dx,dy
case1=[
    [(1,0),(1,1)],[(1,1),(1,2)],[(0,0),(0,1)],[(0,1),(0,2)],
    [(0,2),(1,0)],[(0,0),(1,2)],
    [(0,0),(0,2)],[(1,0),(1,2)],
]
#3*2
case2=[
    [(0,1),(1,1)],[(1,1),(2,1)],[(0,0),(1,0)],[(1,0),(2,0)],
    [(0,1),(2,0)],[(0,0),(2,1)],
    [(0,0),(2,0)],[(0,1),(2,1)],
]

answer=0
# 1*4
for i in range(0,N):
    for j in range(0,M-3):
        total=sum(matrix[i][j:j+4])
        answer=max(answer,total)
#4*1
for i in range(0,N-3):
    for j in range(0,M):
        total=matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+3][j]
        answer=max(answer,total)
#2*2
for i in range(0,N-1):
    for j in range(0,M-1):
        total=sum(matrix[i][j:j+2])+sum(matrix[i+1][j:j+2])
        answer=max(answer,total)
#2*3
for i in range(0,N-1):
    for j in range(0,M-2):
        total_of_6=sum(matrix[i][j:j+3])+sum(matrix[i+1][j:j+3])
        for case in case1:
            total=total_of_6
            for k in range(2):
                dx,dy=case[k][0],case[k][1]
                total-=matrix[i+dx][j+dy]
            answer=max(answer,total)
#3*2
for i in range(0,N-2):
    for j in range(0,M-1):
        total_of_6=sum(matrix[i][j:j+2])+sum(matrix[i+1][j:j+2])+sum(matrix[i+2][j:j+2])
        for case in case2:
            total=total_of_6
            for k in range(2):
                dx,dy=case[k][0],case[k][1]
                total-=matrix[i+dx][j+dy]
            answer=max(answer,total)

print(answer)
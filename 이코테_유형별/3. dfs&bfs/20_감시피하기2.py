from itertools import combinations

matrix=[]
teachers=[]
N=int(input())
for i in range(N):
    matrix.append(list(input().split()))
    for j in range(N):
        if matrix[i][j]=='T':
            teachers.append((i,j))

def cvtToPoint(o):
    return o//N,o%N

def isEmpty(x,y):
    return matrix[x][y]=='X'

def isCompleted():
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    for tx,ty in teachers:
        for d in range(4): #상,하,좌,우
            nx,ny=tx+dx[d],ty+dy[d]
            while 0<=nx<N and 0<=ny<N:
                if matrix[nx][ny]=='S':
                    return False
                elif matrix[nx][ny]=='O' or matrix[nx][ny]=='T':
                    break
                else:
                    nx,ny=nx+dx[d],ny+dy[d]
    return True

flag=False
obj_candidates=list(combinations(range(N*N),3))
for objects in obj_candidates:
    x1,y1=cvtToPoint(objects[0])
    x2,y2=cvtToPoint(objects[1])
    x3,y3=cvtToPoint(objects[2])

    if isEmpty(x1,y1) and isEmpty(x2,y2) and isEmpty(x3,y3):
        matrix[x1][y1]='O'
        matrix[x2][y2]='O'
        matrix[x3][y3]='O'

        if isCompleted():
            flag=True
            break

        matrix[x1][y1]='X'
        matrix[x2][y2]='X'
        matrix[x3][y3]='X'

print('YES') if flag else print('NO')
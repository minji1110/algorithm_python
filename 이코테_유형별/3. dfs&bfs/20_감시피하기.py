import sys
from itertools import combinations
def input(): return sys.stdin.readline().rstrip()

N=int(input())
matrix=[['X']*N for _ in range(N)]
for i in range(N):
    matrix[i]=list(input().split())

def check_student(x,y):
    #왼
    for i in range(y-1,-1,-1):
        if matrix[x][i]=='O':
            break
        elif matrix[x][i]=='T':
            return False
        else:
            continue
    #오
    for i in range(y+1,N):
        if matrix[x][i]=='O':
            break
        elif matrix[x][i]=='T':
            return False
        else:
            continue
    #위
    for i in range(x-1,-1,-1):
        if matrix[i][y]=='O':
            break
        elif matrix[i][y]=='T':
            return False
        else:
            continue
    #아래
    for i in range(x+1,N):
        if matrix[i][y]=='O':
            break
        elif matrix[i][y]=='T':
            return False
        else:
            continue
    return True

def is_possible():
    for i in range(N):
        for j in range(N):
            if matrix[i][j]=='S':
                if not check_student(i,j):
                    return False
                
    return True

def simulate():
    possible=False
    
    cases=list(combinations(range(N*N),3))
    for case in cases:
        ix,iy=case[0]//N,case[0]%N
        jx,jy=case[1]//N,case[1]%N
        kx,ky=case[2]//N,case[2]%N

        if matrix[ix][iy]!='X' or matrix[jx][jy]!='X' or matrix[kx][ky]!='X':
            continue
        matrix[ix][iy]=matrix[jx][jy]=matrix[kx][ky]='O'

        if is_possible():
            possible=True
            break
        else:
            matrix[ix][iy]=matrix[jx][jy]=matrix[kx][ky]='X'
    return possible
    
answer = simulate()
if answer:
    print('YES')
else:
    print('NO')
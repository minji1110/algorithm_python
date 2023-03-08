import sys
def input(): return sys.stdin.readline().rstrip()

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

N,M,K=map(int,input().split())
matrix=[[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    matrix[r-1][c-1].append([m,s,d]) #[질량,속력,방향]

def move_all_fireballs():
    global matrix
    result=[[[] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            fireballs=matrix[i][j]
            for k in range(len(fireballs)):
                m,s,d=fireballs[k]
                nx,ny=(i+s*dx[d])%N,(j+s*dy[d])%N
                result[nx][ny].append([m,s,d])
    return result

def combine_fireballs(i,j):
    global matrix
    
    fireballs=matrix[i][j]
    total_m,total_s=0,0
    even_or_odd=[0,0]

    for k in range(len(fireballs)):
        even_or_odd[fireballs[k][2]%2]+=1
        total_m+=fireballs[k][0]
        total_s+=fireballs[k][1]
    
    m=total_m//5
    s=total_s//len(fireballs)
    d_list=[] 
    if even_or_odd[0]==0 or even_or_odd[1]==0:
        d_list=[0,2,4,6]
    else:
        d_list=[1,3,5,7]

    result=[]
    if total_m!=0:
        for k in range(4):
            result.append([m,s,d_list[k]])
    return result


for _ in range(K):
    matrix=move_all_fireballs()

    for i in range(N):
        for j in range(N):
            if len(matrix[i][j])>1:
                matrix[i][j]=combine_fireballs(i,j)

answer=0
for i in range(N):
    for j in range(N):
        for fb in matrix[i][j]:
            answer+=fb[0]
print(answer)
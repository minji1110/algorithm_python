import sys
def input(): return sys.stdin.readline().rstrip()

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

N,M,K=map(int,input().split())
matrix=[[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    matrix[r-1][c-1].append([m,s,d]) #[질량,속력,방향]

def print_matrix():
    for i in range(N):
        print(matrix[i])
    print("========================")
# 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
# 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
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

# 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    # 파이어볼은 4개의 파이어볼로 나누어진다.
    # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    # 질량이 0인 파이어볼은 소멸되어 없어진다.
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

    print_matrix()

    for i in range(N):
        for j in range(N):
            if len(matrix[i][j])>1:
                matrix[i][j]=combine_fireballs(i,j)
    
    print_matrix()

# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
answer=0
for i in range(N):
    for j in range(N):
        for fb in matrix[i][j]:
            answer+=fb[0]
print(answer)
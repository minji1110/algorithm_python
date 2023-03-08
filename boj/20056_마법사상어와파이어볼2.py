import sys
def input(): return sys.stdin.readline().rstrip()

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

N,M,K=map(int,input().split())
matrix=[[[] for _ in range(N)]for _ in range(N)]

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    matrix[r-1][c-1].append((m,s,d))

for _ in range(K):
    new_matrix=[[[] for _ in range(N)]for _ in range(N)]
    # 이동
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                for k in range(len(matrix[i][j])):
                    m,s,d=matrix[i][j][k]
                    nx=(i+(dx[d]*s))%N
                    ny=(j+(dy[d]*s))%N
                    new_matrix[nx][ny].append((m,s,d))
    matrix=new_matrix

    # 2개 이상인 경우 처리
    for i in range(N):
        for j in range(N):
            num_of_fireballs=len(matrix[i][j])
            if num_of_fireballs>=2:
                total_m=0
                total_s=0
                cnt_odd,cnt_even=0,0
                
                for k in range(num_of_fireballs):
                    fireball=matrix[i][j][k]
                    total_m+=fireball[0]
                    total_s+=fireball[1]
                    if (fireball[2]%2)==0:
                        cnt_even+=1
                    else:
                        cnt_odd+=1

                result=[]
                new_m=total_m//5
                new_s=total_s//num_of_fireballs
                
                if new_m==0: # 질량이 0인 경우
                    matrix[i][j]=[]
                    continue     
                
                d_list=[]
                if cnt_even==0 or cnt_odd==0:
                    d_list=[0,2,4,6]
                else:
                    d_list=[1,3,5,7]

                for dir in d_list:
                    result.append((new_m,new_s,dir))                
                matrix[i][j]=result
answer=0
for i in range(N):
    for j in range(N):
        for fireball in matrix[i][j]:
            answer+=fireball[0]
print(answer)
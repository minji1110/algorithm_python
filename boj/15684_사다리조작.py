from itertools import combinations

N,M,H=map(int,input().split())
ladders=[[0]*(N) for _ in range(H)]
for _ in range(M):
    a,b=map(int,input().split())
    ladders[a-1][b-1]=1

# 사다리타기 -> i번째 결과 i인지 확인
def simulate():
    for i in range(N):
        col=i
        for row in range(H):
            if ladders[row][col]==1:
                col+=1
                continue
            elif col>0 and ladders[row][col-1]==1:
                col-=1
                continue
        if col!=i:
            return False
    return True

if simulate():
    print(0)
else:
    success=False
    for cnt in range(1,4): #놓을 사다리 수
        combi=list(combinations(range(N*H),cnt))

        for candidate in combi:
            valid=True
            for c in candidate:
                i,j=c//N, c%N
                # 사다리 놓을 수 있는지 (가로선 겹치치 않고, 마지막 세로선 아닌지)
                if ladders[i][j]==1 or (j>0 and ladders[i][j-1]==1) or j==N-1:
                    valid=False
                    break
            
            if not valid:
                continue

            for c in candidate:
                i,j=c//N, c%N
                ladders[i][j]=1
    
            success=simulate()
            if success:
                print(cnt)
                break
        
            #원상복귀
            for c in candidate: 
                i,j=c//N,c%N
                ladders[i][j]=0
        if success:
            break
    if not success:
        print(-1)
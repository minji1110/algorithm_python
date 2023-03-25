def solution(m, n, puddles):
    matrix=[[0]*m for _ in range(n)] #경우의수

    # 초기값
    for x,y in puddles:
        matrix[x-1][y-1]=None

    for row in range(1,n):
        if matrix[row][0]==None:
            break
        matrix[row][0]=1

    for col in range(1,m):
        if matrix[0][col]==None:
            break
        matrix[0][col]=1
    
    #dp
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=None:
                upper=matrix[i-1][j]
                left=matrix[i][j-1]

                if upper==left==None:
                    matrix[i][j]=None
                elif upper==None:
                    matrix[i][j]=left%1000000007
                elif left==None:
                    matrix[i][j]=upper%1000000007
                else:
                    matrix[i][j]=(upper+left)%1000000007
    
    answer=matrix[n-1][m-1]
    return answer

m=4
n=3
# puddles=[[2,2]]
puddles=[]
print(solution(m,n,puddles))
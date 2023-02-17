def solution(triangle):
    n=len(triangle)
    answer = 0
    dp=[[0]*n for _ in range(n)]
    dp[0][0]=triangle[0][0]
    
    for i in range(1,n):
        for j in range(len(triangle[i])):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            elif j==len(triangle[i])-1:
                dp[i][j]=dp[i-1][len(triangle[i-1])-1]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    answer=max(dp[n-1])
    return answer

# triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
triangle=[[4],[0,0],[500,600]]
print(solution(triangle))
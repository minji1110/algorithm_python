def solution(n, s, a, b, fares):
    INF=1e9
    answer=INF
    distance_matrix = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        distance_matrix[i][i]=0 
    
    for c,d,f in fares:
        distance_matrix[c][d]=f
        distance_matrix[d][c]=f

    for k in range(1,n+1):
        for v1 in range(1,n+1):
            for v2 in range(1,n+1):
                if distance_matrix[v1][v2]> distance_matrix[v1][k]+distance_matrix[k][v2]:
                    distance_matrix[v1][v2]=distance_matrix[v1][k]+distance_matrix[k][v2]
    
    for share in range(1,n+1): # s로부터 share까지 같이 탐
        if answer>distance_matrix[s][share]+distance_matrix[share][a]+distance_matrix[share][b]:
            answer= distance_matrix[s][share]+distance_matrix[share][a]+distance_matrix[share][b]
    return answer

n,s,a,b=6,4,6,2	
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n,s,a,b=7,3,4,1
fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n,s,a,b=6,4,5,6
fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n,s,a,b,fares))
# 기본 dfs

## 인접 리스트 이용
def dfs_list(graph, visited, v):
    visited[v]=True
    print(v, end=' ')
    
    for adjacent in graph[v]:
        if not visited[adjacent]:
            dfs_list(graph,visited,adjacent)


## 인접 행렬 이용
def dfs_matrix(matrix, visited, v):
    visited[v]=True
    print(v,end=' ')

    for i in range(1,9):
        if matrix[v][i] and (not visited[i]):
            dfs_matrix(matrix, visited, i)


graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

matrix=[
    [False, False, False, False, False, False, False, False, False],
    [False, False, True, True, False, False, False, False, True],
    [False, True, False, False, False, False, False, True, False],
    [False, True, False, False, True, True, False, False, False],
    [False, False, False, True, False, True, False, False, False],
    [False, False, False, True, True, False, False, False, False],
    [False, False, False, False, False, False, False, True, False],
    [False, False, True, False, False, False, True, False, True],
    [False, True, False, False, False, False, False, True, False]
    ]


visited_list=[False]*len(graph)
visited_matrix=[False]*len(matrix)

dfs_list(graph,visited_list,1)
print()
dfs_matrix(matrix, visited_matrix, 1)
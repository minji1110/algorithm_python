# 기본 bfs
from collections import deque

def bfs_list(graph, visited, start):
    q_list=deque()
    q_list.append(start)
    visited[start]=True

    while q_list:
        v=q_list.popleft()
        print(v, end=' ')

        for adjacent in graph[v]:
            if not visited[adjacent]: 
                visited[adjacent]=True
                q_list.append(adjacent)


def bfs_matrix(matrix, visited, start):
    q_matrix=deque()
    q_matrix.append(start)
    visited[start]=True

    while q_matrix:
        v=q_matrix.popleft()
        print(v, end=' ')

        for i in range(1,len(matrix)):
            if matrix[v][i] and not visited[i]:
                visited[i]=True
                q_matrix.append(i)


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

bfs_list(graph, visited_list, 1)
print()
bfs_matrix(matrix, visited_matrix, 1)
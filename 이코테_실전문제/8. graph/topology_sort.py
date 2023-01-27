# 위상 정렬 알고리즘
# 순서가 정해진 작업을 처리할 때 사용
# 즉, 방향 그래프의 노드를 순서대로 나열할 수 있음
# 진입차수(indegree) + 큐 를 이용 , 진입차수 = 0 인 노드를 큐에 넣고, 
# 해당 노드로부터 나가는 간선을 삭제함. 이를 반복!

from collections import deque

nv,ne=map(int, input().split())
graph = [[] for _ in range(nv+1)]
indegree_graph = [0] * (nv+1)

for _ in range(ne):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree_graph[b]+=1


topology=[]
q=deque()

for i in range(1,nv+1):
    if indegree_graph[i]==0:
        q.append(i)
        topology.append(i)

while q:
    v=q.popleft()

    for adjacent in graph[v]:
        indegree_graph[adjacent]-=1
    
    for i in range(1,nv+1):
        if indegree_graph[i]==0 and (i not in topology):
            q.append(i)
            topology.append(i)

print(topology)

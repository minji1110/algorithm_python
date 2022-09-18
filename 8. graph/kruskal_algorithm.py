# 크루스칼 알고리즘 : 그래프 주어질 때, 가장 적은 비용의 신장트리 찾기
# 신장트리 : 모든 노드를 포함하면서 사이클이 존재하지 않는 부분그래프 
# 모든 간선을 비용순으로 정렬, 작은 비용부터 두 노드 union (사이클 있을경우 union x)

def find_root(root_table, x):
    if root_table[x]!=x:
        root_table[x]=find_root(root_table,root_table[x])
    return root_table[x]

def union(root_table,root_a,root_b):
    if root_a<root_b : root_table[root_b]=root_a
    else : root_table[root_a]=root_b

nv,ne=map(int, input().split())
root_table = [i for i in range(nv+1)] 

weight_table=[]
total_weights=0

for _ in range(ne):
    a,b,weight=map(int,input().split())
    weight_table.append((weight,a,b))

weight_table.sort()

for i in range(ne):
    weight, a, b = weight_table[i]
    root_a = find_root(root_table,a)
    root_b=find_root(root_table,b)

    if root_a!=root_b:
        total_weights+=weight
        union(root_table,root_a,root_b)

print(total_weights)



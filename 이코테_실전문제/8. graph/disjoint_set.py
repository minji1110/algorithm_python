# 서로소 집합 찾기 : union & find 이용
# 각 노드의 부모테이블을 유지 , 간선이 존재하는 두 노드 = 같은 부모 같도록 설정

def find_root(parent_table, x):
    if parent_table[x]!=x:
        parent_table[x]=find_root(parent_table,parent_table[x])
    return parent_table[x]

def union(parent_table,a,b):
    parent_a = find_root(parent_table,a)
    parent_b = find_root(parent_table,b)
    if parent_a<parent_b : parent_table[b]=parent_a
    else : parent_table[a]=parent_b

nv,ne=map(int, input().split())
parent_table = [i for i in range(nv+1)] # 0 ~ nv

for _ in range(ne):
    a,b = map(int, input().split())
    union(parent_table,a,b)

print('root :', end=' ')
for i in range(1,nv+1):
    print(find_root(parent_table, i),end=' ')


print('\nparent table :', end=' ')
for i in range(1,nv+1):
    print(parent_table[i],end=' ')
# '무방향' 그래프에서의 사이클 판별 : find & union 이용
# 인접한 두 노드간 union 처리, 이미 root 가 같은 경우 사이클 발생한 것!

def find_root(root_table, x):
    if root_table[x]!=x:
        root_table[x]=find_root(root_table,root_table[x])
    return root_table[x]

def union(root_table,root_a,root_b):
    if root_a<root_b : root_table[root_b]=root_a
    else : root_table[root_a]=root_b
    
nv,ne=map(int, input().split())
root_table = [i for i in range(nv+1)] 

has_cycle = False

for _ in range(ne):
    a,b=map(int, input().split())
    root_a = find_root(root_table,a)
    root_b=find_root(root_table, b)

    if(root_a == root_b) : 
        has_cycle=True
        print('cycle 이 존재합니다.')
        break
    else:
        union(root_table,root_a,root_b)

if(has_cycle==False):
    print('cycle이 존재하지 않습니다.')
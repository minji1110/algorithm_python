import sys
def input():return sys.stdin.readline().rstrip()

nv,ne=map(int,input().split())
root_table = [i for i in range(nv+1)]

def find_root(x):
    if x!=root_table[x]:
        root_table[x]=find_root(root_table[x])
    return root_table[x]

def union(root_a,root_b):
    if root_a<root_b : root_table[root_b]=root_a
    else : root_table[root_a]=root_b

weight_table=[]
for _ in range(ne):
    a,b,weight = map(int, input().split())
    weight_table.append((weight,a,b))

weight_table.sort()
total_weight=0
last_weight=0

for i in range(ne):
    weight,a,b=weight_table[i]
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a!=root_b:
        union(root_a,root_b)
        total_weight+=weight
        last_weight=weight

print(total_weight-last_weight)

    

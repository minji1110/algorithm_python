import sys
from itertools import combinations
def input(): return sys.stdin.readline().rstrip()

N,M=map(int,input().split())
matrix=[] # 도시
houses=[] # 집들의 좌표
chickens=[] # 치킨 집들의 좌표
selected_chickens=[]

for i in range(N):
    row=list(map(int,input().split()))
    matrix.append(row)
    for j in range(N):
        if matrix[i][j]==1:
            houses.append((i,j))
        elif matrix[i][j]==2:
            chickens.append((i,j))

# 한 집의 최소 치킨거리 반환
def get_chicken_distance(hx,hy):
    result=2*N
    for cx,cy in selected_chickens:
        distance=abs(cx-hx)+abs(cy-hy)
        result=min(result,distance)
    return result

# 도시의 치킨거리 반환
def get_city_chicken_distance():
    result=0
    for hx,hy in houses:
        chicken_distance=get_chicken_distance(hx,hy)
        result+=chicken_distance
    return result

# M개 고르는 경우의 수에 대해 최소값 도출
answer=1e9
for combi in list(combinations(chickens,M)):
    selected_chickens=combi
    city_chicken_distance=get_city_chicken_distance()
    answer=min(answer,city_chicken_distance)

print(answer)
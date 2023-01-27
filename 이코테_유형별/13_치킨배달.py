import sys
from itertools import combinations
def input(): return sys.stdin.readline().rstrip()

N,M=map(int,input().split())
city=[]
houses=[] # 집들 좌표
chickens=[] # 치킨집들 좌표
selected_chickens=[]
answer=1e9

# 각 집의 치킨거리를 구합니다.
def get_chicken_distance(hx,hy):
    global selected_chickens
    min_value=1e9

    for cx,cy in selected_chickens:
        chicken_distance = abs(hx-cx)+abs(hy-cy)
        min_value=min(min_value,chicken_distance)

    return min_value


# 도시의 치킨거리를 구합니다.
def get_chicken_distance_of_city():
    global houses
    
    chiken_distance_of_city=0
    for hx,hy in houses:
        chicken_distance = get_chicken_distance(hx,hy)
        chiken_distance_of_city+=chicken_distance
    
    return chiken_distance_of_city

for i in range(N):
    city.append(list(map(int,input().split())))
    for j in range(N):
        if city[i][j]==2:
            chickens.append((i,j))
        elif city[i][j]==1:
            houses.append((i,j))

# M개의 치킨집 선택
for selected in list(combinations(chickens,M)): 
    selected_chickens=list(selected)    
    
    cd=get_chicken_distance_of_city()
    answer=min(answer,cd)

print(answer)

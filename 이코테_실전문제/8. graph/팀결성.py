import sys
def input():return sys.stdin.readline().rstrip()

n,m=map(int,input().split())
team_table=[i for i in range(n+1)] # 0 ~ n 

# 팀 찾기
def find_team(x):
    if x!=team_table[x]:
        team_table[x]=find_team(team_table[x])
    return team_table[x]

# 팀 합치기
def merge_team(a,b):
    team_a= find_team(a)
    team_b= find_team(b)
    if team_a<team_b:
        team_table[team_b]=team_a
    else:
        team_table[team_a]=team_b

# 같은 팀 여부 확인
def isSameTeam(a,b):
    if(find_team(a) == find_team(b)):
        return 'YES'
    else:
        return 'NO'

for _ in range(m):
    action,a,b=map(int,input().split())
    if action == 0:
        merge_team(a,b)
    else:
        print(isSameTeam(a,b))


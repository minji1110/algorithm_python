import sys
def input(): return sys.stdin.readline().rstrip()

data=list(map(int,input()))
group=[0,0] # 0 그룹 수, 1 그룹 수

now=data[0]
group[now]+=1

for i in range(1,len(data)):
    if now!=data[i]:
        group[now]+=1
        now=data[i]

print(min(group[0],group[1]))





# 이것이 코딩테스트다 4-1. 상하좌우
n=int(input())
plan=list(input().split())

nowX=1
nowY=1

for i in range(0,len(plan)):
  next=plan[i]
  if (next=='R' and nowY+1<=n):
    nowY+=1
  elif(next=='L' and nowY-1>=1):
    nowY-=1
  elif(next=='U' and nowX-1>=1):
    nowX-=1
  elif(next=='D' and nowX+1<=n):
    nowX+=1

print(nowX,nowY)
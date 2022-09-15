# 이것이 코딩테스트다 4-4. 게임개발

n,m=map(int,input().split())
nowX, nowY, direction=map(int,input().split()) #현재x,y좌표 / 보고있는 방향
cnt=1

#북,동,남,서 순서 
left_dx=[0,-1,0,1]
left_dy=[-1,0,1,0]
back_dx=[1,0,-1,0]
back_dy=[0,-1,0,1]

#map 생성
matrix=[]
for i in range(0,n):
  matrix.append(list(map(int,input().split())))

matrix[nowX][nowY]=2
noMore=False

while(True):
  for i in range(0,4):
    dx=left_dx[direction]
    dy=left_dy[direction]

    #왼쪽으로 갈 수 있음
    if(matrix[nowX+dx][nowY+dy]==0):
      nowX+=dx
      nowY+=dy
      matrix[nowX][nowY]=2
    
      direction=(direction-1) if (direction>0) else 3
      cnt+=1
      break

    else:
      direction=(direction-1) if (direction>0) else 3
      if(i==3) : noMore=True
      
  #뒤로, 바다인경우 멈춤
  if(noMore):
    backX=back_dx[direction]
    backY=back_dy[direction]
    if(matrix[nowX+backX][nowY+backY]==1):
      break
    else :
      nowX,nowY=nowX+backX, nowY+backY
      noMore=False
      
      
print(cnt)
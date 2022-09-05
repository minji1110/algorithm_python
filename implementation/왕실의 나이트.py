#이것이 코딩테스트다 4-3. 왕실의 나이트

# 오2위1 , 오2아1 , 왼2위1 , 왼2아1
# 위2오1 , 위2왼1 , 아2오1 , 아2왼1
dx=[+1,-1,+1,-1,+2,+2,-2,-2]
dy=[+2,+2,-2,-2,+1,-1,+1,-1]

input=input()
row=int(input[1])
col=ord(input[0])-ord('a')+1

cnt=0
for i in range(8):
  if(1<=(row+dx[i])<=8 and 1<=(col+dy[i])<=8):
    cnt+=1

print(cnt)
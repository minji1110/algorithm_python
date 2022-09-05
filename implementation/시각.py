# 이것이 코딩테스트다 4-2. 시각 
# n시 59분 59초

n=int(input())
cnt=0

for h in range(0,n+1):
  if('3' in str(h)):
    cnt+=3600
    continue
  for m in range(0,60):
    if('3' in str(m)):
      cnt+=60
      continue
    for s in range(0,60):
      if('3' in str(s)):
        cnt+=1
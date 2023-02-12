import math

def get_combination(n,r):
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

n,m=map(int,input().split())
data=list(map(int,input().split()))
balls=[0]*(m+1)

for i in data:
    balls[i]+=1

answer=get_combination(n,2)
for ball in balls:
    if ball>1:
        answer-=get_combination(ball,2)

print(answer)




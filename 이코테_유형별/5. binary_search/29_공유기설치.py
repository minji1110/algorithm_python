import sys
def input(): return sys.stdin.readline().rstrip()

def possible(target_answer):
    cnt=1
    prev=houses[0]
    for i in range(1,len(houses)):
        if houses[i]-prev>=target_answer:
            cnt+=1
            prev=houses[i]
            if cnt==c:
                return True
    return False


def bs(start,end):
    global answer

    if start>end:
        return
    
    mid= (start+end)//2
    if possible(mid):
        answer=mid
        bs(mid+1,end)
    else:
        bs(start,mid-1)
           
n,c=map(int,input().split())
houses=[]
answer=0

for _ in range(n):
    houses.append(int(input()))
houses.sort()

if c==2:
    print(houses[n-1]-houses[0])
else:
    bs(1,houses[n-1]-houses[0])
    print(answer)

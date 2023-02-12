n=int(input())
arr=list(map(int,input().split()))
arr.sort()

cnt=0
answer=0
for i in range(n):
    cnt+=1
    now=arr[i]
    if cnt>=arr[i]:
        answer+=1
        cnt=0

print(answer)

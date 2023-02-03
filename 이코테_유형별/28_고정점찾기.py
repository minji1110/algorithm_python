n=int(input())
arr=list(map(int,input().split()))

def bs(start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if mid==arr[mid]:
        return mid
    elif arr[mid] + (n-1-mid) > n-1:
        return bs(start,mid-1)
    elif arr[mid]-mid<0:
        return bs(mid+1,end)
    else:
        answer = bs(start,mid-1)
        if answer==-1:
            answer=bs(mid+1,end)
        return answer

print(bs(0,n-1))
def find_left(start,end):
    global array, x
    if start>end:
        return -1
    
    mid=(start+end)//2
    if array[mid]==x and (mid>0 and array[mid-1]<x):
        return mid
    elif array[mid]<x:
        start=mid+1
        return find_left(start,end)
    else:
        end=mid-1
        return find_left(start,end)


def find_right(start,end):
    global array, x, n
    if start>end:
        return -1
    
    mid=(start+end)//2
    if array[mid]==x and (mid<n-1 and array[mid+1]>x):
        return mid
    elif array[mid]<=x:
        start=mid+1
        return find_right(start,end)
    else:
        end=mid-1
        return find_right(start,end)

n,x=map(int,input().split())
array=list(map(int,input().split()))

left=find_left(0,n-1)
if left!=-1:
    right=find_right(0,n-1)
    print(right-left+1)
else:
    print(-1)


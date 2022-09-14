# 이코테 - 이진탐색 : 부품찾기
import sys

n=int(sys.stdin.readline().rstrip())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))

m=int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

for m in m_arr:
    if m in n_arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()

## bs 이용
def binary_search(array, target, start, end):
    if start>end:
        return -1
    else :
        mid = (start+end) // 2
        if array[mid] == target: 
            return mid
        elif array[mid]<target:
            return binary_search(array, target, mid+1, end)
        else:
            return binary_search(array,target,start,mid-1)

n_arr.sort()
for m in m_arr:
    if(binary_search(n_arr, m, 0,len(n_arr)-1) == -1):
        print('no', end=' ')
    else:
        print('yes',end=' ')


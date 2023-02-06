import sys
def input(): return sys.stdin.readline().rstrip()

n,m=map(int,input().split())
higher=[[] for _ in range(n+1)]
lower=[[] for _ in range(n+1)]

def get_higher(arr,i):
    if not higher[i]:
        return arr

    for high in higher[i]:
        if high not in arr:
            arr.append(high)
        arr = get_higher(arr,high)
    return arr

def get_lower(arr,i):
    if not lower[i]:
        return arr

    for low in lower[i]:
        if low not in arr:
            arr.append(low)
        arr=get_lower(arr,low)
    return arr

for _ in range(m):
    low,high = map(int,input().split())
    higher[low].append(high)
    lower[high].append(low)

print('higher=',higher)
print('lower=',lower)
answer=0

for i in range(1,n+1):
    h_arr=higher[i][:]
    h_arr = get_higher(h_arr,i)

    l_arr = lower[i][:]
    l_arr = get_lower(l_arr,i)
    
    print('i=',i)
    print('h_arr=',h_arr)
    print('l_arr=',l_arr)

    if len(h_arr)+ len(l_arr)== n-1:
        answer+=1

print(answer)

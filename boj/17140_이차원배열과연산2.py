import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

r,c,k=map(int,input().split())
r,c=r-1,c-1
A=[[0]*100 for _ in range(100)]
row_len,col_len=3,3

for i in range(3):
    data=list(map(int,input().split()))
    A[i][0],A[i][1],A[i][2]=data

def calculate(type):
    global A,row_len,col_len
    max_length=0

    for i in range(len(A)):
        exist_nums=[]
        cnts=[0]*101
        for num in A[i]:
            if num==0:
                continue
            if num not in exist_nums:
                exist_nums.append(num)
            cnts[num]+=1
        
        pq=[]
        for en in exist_nums:
            heapq.heappush(pq,(cnts[en],en)) #(횟수, 숫자)
        
        result=[]
        while pq:
            count,number=heapq.heappop(pq)
            result.append(number)
            result.append(count)

            if len(result)==100:
                break
        
        max_length=max(max_length,len(result))
        for _ in range(len(result),100):
            result.append(0)
        A[i]=result
    
    if type=='R':
        col_len=max_length
    else:
        row_len=max_length

t=0
while True:
    if A[r][c]==k:
        print(t)
        break
    if t==100:
        print(-1)
        break

    if row_len>=col_len:
        calculate('R')
    else:
        A=list(map(list,zip(*A)))
        calculate('C')
        A=list(map(list,zip(*A)))
    
    t+=1
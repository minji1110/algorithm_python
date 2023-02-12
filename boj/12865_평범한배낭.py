# 시간초과
import sys
def input(): return sys.stdin.readline().rstrip()

n,k=map(int,input().split())
stuffs=[]

def dfs(index,w_sum,v_sum,v_rest):
    global maximum    

    if index==n-1 or w_sum+stuffs[index+1][0]>k : # 내가 마지막
        maximum=max(maximum, v_sum)
        return
    
    if v_sum+v_rest<=maximum:
        return
    
    # 다음 무게 포함O
    dfs(index+1,w_sum+stuffs[index+1][0],v_sum+stuffs[index+1][1],v_rest-stuffs[index+1][1]) 
    # 다음 무게 포함X
    dfs(index+1,w_sum,v_sum,v_rest-stuffs[index+1][1])

values_sum=0
for _ in range(n):
    w,v=map(int,input().split())
    values_sum+=v
    stuffs.append((w,v))

stuffs.sort()
maximum=0

if stuffs[0][0]<=k:
    dfs(0,stuffs[0][0],stuffs[0][1],values_sum-stuffs[0][1])
    dfs(0,0,0,values_sum-stuffs[0][1])

print(maximum)
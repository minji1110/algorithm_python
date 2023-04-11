# nPm itertools 없이 구현하기
N,M=map(int,input().split())
arr=[]
visited=[False]*(N+1)

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
def back_tracking():
    if len(arr)==M:
        for x in arr:
            print(x,end=' ')
        print()
        return

    for x in range(1,N+1):
        if not visited[x]:
            visited[x]=True
            arr.append(x)
            back_tracking()
            arr.pop()
            visited[x]=False

back_tracking()
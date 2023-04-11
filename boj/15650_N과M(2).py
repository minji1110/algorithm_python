# nCm
N,M=map(int,input().split())
arr=[]

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열. 고른 수열은 오름차순이어야 한다.
def back_tracking(tmp):
    if len(arr)==M:
        for x in arr: print(x,end=' ')
        print()

    for i in range(len(tmp)):
        arr.append(tmp[i])
        back_tracking(tmp[i+1:])
        arr.pop()

back_tracking([i for i in range(1,N+1)])
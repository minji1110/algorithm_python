import sys
def input():return sys.stdin.readline().rstrip()

N,M=map(int, input().split())   # N개, 최대 Mkg
balls = list(map(int, input().split()))

accum_list = [0 for _ in range(M+1)]
for b in balls:
    accum_list[b]+=1

# 2개 고르기
cnt=0
for left in range(1,M):
    for right in range(left+1,M+1):
        cnt+=(accum_list[left]*accum_list[right])

print(cnt)


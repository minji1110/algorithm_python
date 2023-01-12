import sys 
def input() : return sys.stdin.readline().rstrip()

score=list(map(int,input()))
N=len(score)

left = sum(score[:N//2])
right=sum(score[N//2:])

if left==right:
    print('LUCKY')
else:
    print('READY')


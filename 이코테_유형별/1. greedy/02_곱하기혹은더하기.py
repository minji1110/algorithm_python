import sys
def input():return sys.stdin.readline().rstrip()

s=list(map(int,input()))
answer=s[0]

for i in range(1,len(s)):
    if answer<=1 or s[i]==0:
        answer+=s[i]
    else:
        answer*=s[i]

print(answer)

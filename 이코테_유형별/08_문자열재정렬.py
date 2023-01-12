import sys 
def input() : return sys.stdin.readline().rstrip()

s=list(input())
s.sort()

cnt=0
start=0

for i in range(len(s)):
    if ord(s[i])<65 :
        cnt+=int(s[i])
        if i==len(s)-1:
            start=len(s)
    else:
        start=i
        break

# 특수조건 잘 생각하기 !!
if cnt!=0:
    answer=''.join(s[start:])+str(cnt)
else:
    answer=''.join(s[start:])

print(answer)
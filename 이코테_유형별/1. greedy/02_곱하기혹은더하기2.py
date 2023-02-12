s=list(map(int,input()))
answer=s[0]

for i in range(1,len(s)):
    if answer==0 or answer==1 or s[i]==0 or s[i]==1:
        answer+=s[i]
    else:
        answer*=s[i]

print(answer)
def solution(s):
    n=len(s)
    answer = n

    for k in range(1,n//2+1): #k개로 자르는 경우
        repeated=1
        length=0
        prev=s[0:k]

        for i in range(1,n//k):
            now=s[i*k:(i+1)*k]
            if prev==now:
                repeated+=1
                continue
            else:
                length+=k
                if repeated>1:
                    length+=len(str(repeated))
                repeated=1
                prev=now
        
        # 마지막 문자열
        if repeated>1:
            length+=len(str(repeated))
        length+=k
        # 남은 문자열
        length+=n%k 
        answer=min(answer,length)    
    return answer

s="aaaaaaaaaabbbbbbbbbb"
# s="ababcdcdababcdcd"
# s="abcabcdede"
# s="abcabcabcabcdededededede"
# s="xababcdcdababcdcd"
print(solution(s))
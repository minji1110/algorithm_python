s="aaaaaaaaaabbbbbbbbbb"
# s="ababcdcdababcdcd"
# s="abcabcdede"
# s="abcabcabcabcdededededede"
# s="xababcdcdababcdcd"

def solution(s):
    answer = len(s)
    
    length=len(s)
    maximum_n = length//2

    # n 개로 자르는 경우
    for n in range(1,maximum_n+1):
        print('n= ',n) 
        n_answer=0
        dupl_cnt=0
        prev=""
        
        for start in range(0,length,n):
            if start+n>length:
                end=length
            else:
                end=start+n
            now = s[start:end] 

            # 이전과 다름 
            if prev!=now:
                if dupl_cnt==0:
                    n_answer+=len(prev)
                else: # 이전값 반복된만큼 +   
                    n_answer+=len(prev)+len(str(dupl_cnt+1))
                    dupl_cnt=0
                prev=now # 이전값 업데이트
            # 이전과 같음
            else: 
                dupl_cnt+=1
           
        # 마지막
        if dupl_cnt==0:
            n_answer+=len(prev)
        else:
            n_answer+=len(prev)+len(str(dupl_cnt+1))
        answer=min(answer,n_answer)

    return answer

print(solution(s))
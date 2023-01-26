'''
작업 순서가 정해진경우에는 (특히 문자열 관련 문제 & 앞문제)
일단 그대로 구현하기!!
'''

# 균형잡힌 문자열의 마지막 index
def get_balanced_index(str):
    cnt=0
    for i in range(len(str)):
        if str[i]=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return i

# 올바른 문자열인지 판단
def is_correct(str):
    cnt=0
    for i in range(len(str)):
        if str[i]=='(':
            cnt+=1
        else:
            if cnt==0: 
                return False
            cnt-=1
    return True

def solution(p):
    answer = ''
    if len(p)==0:
        return answer
    
    balanced_index=get_balanced_index(p)
    u=p[:balanced_index+1]
    v=p[balanced_index+1:]

    if is_correct(u):
        answer+=u+solution(v)
    else:
        comp='('+solution(v)+')'
        u=u[1:-1]

        for i in range (len(u)):
            if u[i]=='(':
                comp+=')'
            else:
                comp+='('
        return comp

    return answer

p="()))((()"
print(solution(p))

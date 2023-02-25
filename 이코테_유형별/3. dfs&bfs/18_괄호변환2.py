# 균형잡힌 문자열이 되는 최소 index 를 반환
def get_balanced_index(p):
    cnt=[0,0] #(,)
    for i in range(len(p)):
        if p[i]=='(':
            cnt[0]+=1
        else:
            cnt[1]+=1
        if cnt[0]==cnt[1]:
            return i

# 올바른 문자열인지 반환
def is_correct_string(str):
    cnt=0 #( 의 개수
    for i in range(len(str)):
        if str[i]==')':
            if cnt==0:
                return False
            cnt-=1
        else:
            cnt+=1
    return True

# 괄호의 방향을 뒤집어 반환
def reverse_string(str):
    result=''
    for i in range(len(str)):
        if str[i]=='(':
            result+=')'
        else:
            result+='('
    return result

def solution(p):    
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if len(p)==0:
        return ''
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    balanced_index=get_balanced_index(p)
    u=p[:balanced_index+1]
    v=p[balanced_index+1:]

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    if is_correct_string(u):
        u=u+solution(v)
        return u
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    #   4-3. ')'를 다시 붙입니다. 
    new_str='('+solution(v)+')'
    
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    #   4-5. 생성된 문자열을 반환합니다.
    return new_str+reverse_string(u[1:-1])

plist=["(()())()",")(","()))((()"]
for p in plist:
    print(solution(p))
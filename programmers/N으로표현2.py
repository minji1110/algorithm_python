def solution(N, number):
    answer = -1
    
    cnt_list=[[] for _ in range(9)] #cnt 개로 만들 수 있는 수 배열
    for i in range(1,9):
        value=int(str(N)*i)
        if value==number:
            return i
        if value<32000:
            cnt_list[i].append(value)
    
    for cnt in range(2,9): # cntlist[cnt] 에 추가할 것
        for i in range(1,cnt): # 1<->cnt-1 , 2<-> cnt-2 ,,, 
            for a in cnt_list[i]:
                for b in cnt_list[cnt-i]:

                    results=[a+b,a-b,a*b,a//b]
                    for result in results:
                        if result==number:
                            return cnt
                        if 0<result<=32000 and result not in cnt_list[cnt]:
                            cnt_list[cnt].append(result)
        
    return answer

N=5
number=55
print(solution(N,number))
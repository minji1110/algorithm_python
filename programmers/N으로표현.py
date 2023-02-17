# 실패 (문제이해 잘못함)
import heapq
def solution(N, number):
    cnt_table=[-1]*32001
    hq=[]
    answer = -1

    str_N=str(N)
    while(True):
        print('strN=',str_N)
        if int(str_N)>32000:
            break
        cnt_table[int(str_N)]=len(str_N)
        heapq.heappush(hq,(len(str_N),int(str_N)))
        str_N+=str(N)
    
    while hq:
        cnt, value = heapq.heappop(hq)
        print('cnt,value=',cnt,value)
        if cnt>8:
            break
        if value==number:
            answer=cnt
            break
        
        results=[value+N, value-N, value*N, value//N]
        for result in results:
            if result<=0 or 32000<result or cnt_table[result]>0:
                continue
            cnt_table[result]=cnt+1
            heapq.heappush(hq,(cnt+1,result))
    return answer

N=2
number=512
print(solution(N,number))
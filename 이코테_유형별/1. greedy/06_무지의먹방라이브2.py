# 다시
import heapq

def solution(food_times, k):
    answer=0
    q=[]
    rest=[]
    for i in range(len(food_times)):
        rest.append(i+1)
        heapq.heappush(q,(food_times[i],i+1)) #걸리는 시간, 음식번호
    
    total_t=0
    while q:
        t,index = heapq.heappop(q)

        if (t-total_t)*len(rest)>k:
            heapq.heappush(q,(t,index))
            break
        
        k-=(t-total_t)*len(rest)
        total_t+=1
        rest.remove(index)

    if not rest and k>=0:
        answer=-1
    else:
        answer = rest[k%len(rest)]

    return answer

food_times=[2,2,2,2,2]
k=10
print(solution(food_times,k))
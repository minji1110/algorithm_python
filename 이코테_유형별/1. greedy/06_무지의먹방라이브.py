food_times=[8,6,4]	
k=12

# v1. queue 이용 -> 효율성테스트 실패
from collections import deque

def solution_v1(food_times, k):
    t=0
    q=deque()

    for i in range(0,len(food_times)):
        q.append(((i+1),food_times[i])) # (index, 남은시간)
    
    while(q and t<k):
        t+=1
        index, left_t = q.popleft()
        if left_t>1:
            q.append((index,left_t-1))
    
    if q:
        index, left_t = q.popleft()
        answer = index
    else:
        answer=-1

    return answer

print(solution_v1(food_times, k))


# v2. priority queue 이용
import heapq
def solution_v2(food_times, k):
    answer=0
    if sum(food_times)<=k:
        return -1

    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1)) # (소요시간, 인덱스)
    
    # 남은시간
    left_t = k
    # 이전 소요시간
    prev_t=0
    consumed_t=0
    
    while left_t >= ((q[0][0]-prev_t)*len(q)): # 다음 최소시간 음식을 다 먹을 수 있음. 
        left_t -= ((q[0][0]-prev_t)*len(q)) #(시간 * 음식 개수) 소요됨
        t, index = heapq.heappop(q)
        prev_t = t 
  
    # index 순 정렬 : 전체 길이 len(q) 만큼 곱해서 빼줬으니 어차피 그다음에는 0번차례
    # -> index로 정렬해서 남은 번호에 맞는거 찾으면 됨
    q.sort(key=lambda i:i[1]) 
    index = left_t%len(q)

    answer=q[index][1]
    return answer

print(solution_v2(food_times, k))
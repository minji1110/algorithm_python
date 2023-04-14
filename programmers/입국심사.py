import heapq

# 시간초과 ( 우선순위큐 사용 )
def solution(n, times):
    times.sort()
    if n<=len(times):
        return times[n-1]
    
    answer = 0
    rest=n
    pq=[]
    for i in range(len(times)):
        end_time=times[i]
        heapq.heappush(pq,(end_time,times[i])) #끝나는 시간, 걸리는 시간
        rest-=1
    while rest>0:
        end_time, needed_time = heapq.heappop(pq)
        if rest==1: 
            answer=end_time+needed_time
            break
        heapq.heappush(pq,(end_time+needed_time, needed_time))
        rest-=1
    return answer

# 통과 ( 이분탐색 사용 )
def possible(n,times,mid): # mid시간 내에 모두 처리가능한가
    possible_n=0 # 처리 가능한 사람 수
    for t in times:
        possible_n+= mid//t
        if possible_n>=n : 
            return True
    return False

def solution(n, times):
    answer = 0
    times.sort()

    start=1
    end=times[-1]*n
    while end>=start:
        mid=(start+end)//2
        if possible(n,times,mid):
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer

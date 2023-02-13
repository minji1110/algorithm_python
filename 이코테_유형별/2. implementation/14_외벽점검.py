# 다시 생각해보기
import heapq

# 다음으로 가까운 지점을 반환
def find_next(n,now,weak):
    min_dis,min_index=n,now

    for next in weak:
        if next!=now:
            clock_wise=abs(now-next)
            couter_clock_wise=abs(n-next)+now
            distance=min(clock_wise,couter_clock_wise)
            
            if min_dis>distance:
                min_dis=distance
                min_index=next

    return min_index,min_dis

# 새로운 친구 투입 
def add_new_friend(n,weak,dist,q):
    friend=dist.pop()
    start_weak=heapq.heappop(q)


def solution(n, weak, dist):
    answer = 0
    q=[]
    for w in weak:
        n_index,n_dis=find_next(n,w,weak)
        heapq.heappush(q,(-n_dis,n_index))

    is_ended=False
    while not is_ended:
        is_ended=add_new_friend(n,weak,dist,q)
        answer+=1
        
        if not dist:
            break
    
    if not is_ended:
        answer=-1
    return answer

n=12
weak=[1, 5, 6, 10]
dist=[1,2,3,4]
print(solution(n,weak,dist))
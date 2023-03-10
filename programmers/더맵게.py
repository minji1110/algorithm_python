import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    possible=False

    while scoville:
        first=heapq.heappop(scoville)
        if first>=K:
            possible=True
            break
        if not scoville:
            break

        #섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        second=heapq.heappop(scoville)
        mixed=first+(second*2)
        heapq.heappush(scoville,mixed)
        
        answer+=1

    if not possible:
        answer=-1
    return answer

scoville=[1, 2, 3, 9, 10, 12]
K=7
print(solution(scoville,K))
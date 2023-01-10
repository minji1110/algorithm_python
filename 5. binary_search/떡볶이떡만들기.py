# 이코테 - 이진탐색 : 떡볶이 떡 만들기
import sys

def calc_total_len(ddeok_list, height):
    total_len=0
    for ddeok in ddeok_list:
        total_len += max(0,ddeok-height)
    return total_len

# n = 떡의 개수 / m = 요청 길이
n, m = map(int, sys.stdin.readline().rstrip().split())
ddeok_list=list(map(int, sys.stdin.readline().rstrip().split()))

ddeok_list.sort()
start = 0
end = ddeok_list[n-1]
# 중간에 멈추지 않음! start, end 엇갈릴때까지 수행됨
while(start<=end):
    height = (start+end) // 2

    # 높이 늘려도 됨 (잘린 떡 적어도 됨) => 이 다음에 실패시 이게 정답임
    if calc_total_len(ddeok_list, height) >= m :
        answer=height
        start=height+1
    # 높이 낮춰야함 (잘린 떡 부족함)
    else:
        end=height-1




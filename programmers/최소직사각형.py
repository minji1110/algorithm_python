# 고득점 kit : 완전탐색
def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort(reverse=True)
    sizes.sort(reverse=True)
    
    row_size=sizes[0][0]
    col_size=sizes[0][1]
    
    for i in range(1,len(sizes)):
        if sizes[i][1]>col_size:
            col_size=sizes[i][1]
    
    answer=row_size*col_size
    return answer

# 간단 버전 (시간은 더 오래걸림)
def solution2(sizes):
    answer = 0
    row=max([max(size) for size in sorted(sizes)])
    col=max([min(size) for size in sorted(sizes)])

    answer=row*col
    return answer

sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
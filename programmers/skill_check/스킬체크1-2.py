def solution(lottos, win_nums):
    answer = []
    zero=lottos.count(0)

    matched=0
    for num in lottos:
        if num>0 and num in win_nums:
            matched+=1
            win_nums.remove(num)
    
    min_matched=matched
    max_matched=matched+zero

    matched_to_score=[6,6,5,4,3,2,1]
    answer=[matched_to_score[max_matched],matched_to_score[min_matched]]
    return answer

lottos=[44, 1, 0, 0, 31, 25]
lottos=[45, 4, 35, 20, 3, 0]
win_nums=[20, 9, 3, 45, 4, 34]
print(solution(lottos,win_nums))
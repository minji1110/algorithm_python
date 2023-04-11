def solution(answers):
    students_ans=[
        [1,2,3,4,5], 
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    correct=[0,0,0]
    
    for i in range(len(answers)): # 각 답에 대해
        for j in range(3): # 각 학생의 답과 비교
            answer=answers[i]
            s_answer= students_ans[j][i%len(students_ans[j])]
            if answer==s_answer:
                correct[j]+=1
    
    result=[]
    highest_score=max(correct)
    for i in range(3):
        if correct[i]==highest_score:
            result.append(i+1)
    return result

answers=[1,2,3,4,5]
print(solution(answers))
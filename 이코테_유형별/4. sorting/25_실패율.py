N=5
# N=4
stages=[2, 1, 2, 3, 2, 3, 3, 3]
# stages=[4,4,4,4,4]

def solution(N, stages):
    answer = []
    
    curr_stage=[0]*(N+2)
    for i in range(1,N+2):
        curr_stage[i]=stages.count(i)
    
    challengers=len(stages)
    for i in range(1,N+1):
        if challengers==0:
            fail_rate=0
        else:
            fail_rate = curr_stage[i]/challengers
        
        answer.append((-fail_rate,i))
        challengers-=curr_stage[i]
     
    answer.sort()
    print(answer)
    answer=[i[1] for i in answer]
    
    return answer

print(solution(N,stages))

roads=[]
N,L=map(int,input().split())
for _ in range(N):
    roads.append(list(map(int,input().split())))

# 길을 지나갈 수 있는지 여부 반환
def can_go(road):
    curr_height=road[0]
    passed_cnt=1

    index=1
    while True:
        if index==N:
            break
        
        if road[index]==curr_height:
            passed_cnt+=1
            index+=1
            continue
        #올라감
        elif road[index]-curr_height==1:
            if passed_cnt>=L:
                curr_height=road[index]
                passed_cnt=1
                index+=1
                continue
            else:
                return False
        #내려감
        elif curr_height-road[index]==1: 
            check_list=road[index:index+L] #L개 검사
            if len(check_list)<L:
                return False
            
            for h in check_list:
                if h!=road[index]:
                    return False
                
            curr_height=road[index]
            passed_cnt=0
            index+=L
            continue
        #2이상차이
        else:
            return False
    return True

answer=0
for i in range(N): # 행 검사
    if can_go(roads[i]):
        answer+=1

roads=list(map(list,zip(*roads)))

for i in range(N): # 열 검사
    if can_go(roads[i]):
        answer+=1

print(answer)
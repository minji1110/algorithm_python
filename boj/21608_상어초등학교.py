import sys
def input(): return sys.stdin.readline().rstrip()

N=int(input())
prefer_list=[[] for _ in range(N*N+1)]
students=[[-1]*N for _ in range(N)] 

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 인접한 선호 학생이 많은 자리 리스트를 반환
def get__prefer_candidates(prefers):
    maximum=-1
    result=[]
    
    for x in range(N):
        for y in range(N):
            cnt=0
            if students[x][y]==-1: # 빈자리인 경우에만 확인
                for d in range(4):
                    nx,ny=x+dx[d],y+dy[d]
                    if 0<=nx<N and 0<=ny<N and students[nx][ny] in prefers:
                        cnt+=1
                if cnt>maximum:
                    maximum=cnt
                    result.clear()
                    result.append((x,y))
                elif cnt==maximum:
                    result.append((x,y))
    return result

# 인접한 빈자리가 많은 리스트 반환
def get_empty_candidates(prefer_candidates):
    maximum=-1
    result=[]

    for x,y in prefer_candidates:
        cnt=0
        for d in range(4):
            nx,ny=x+dx[d],y+dy[d]
            if 0<=nx<N and 0<=ny<N and students[nx][ny]==-1:
                cnt+=1
        if cnt>maximum:
            maximum=cnt
            result.clear()
            result.append((x,y))
        elif cnt==maximum:
            result.append((x,y))
    
    return result

# 만족도를 반환. 인접 선호학생 수가 0이면 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
def get_satisfaction():
    point=[0,1,10,100,1000]
    total=0

    for x in range(N):
        for y in range(N):
            cnt=0
            student_index=students[x][y]
            for d in range(4):
                nx,ny=x+dx[d],y+dy[d]
                if 0<=nx<N and 0<=ny<N and students[nx][ny] in prefer_list[student_index]:
                    cnt+=1
            total+=point[cnt]
    return total

order=[]
for _ in range(N*N):
    data=list(map(int,input().split()))
    index=data[0]
    prefers=data[1:]
    
    order.append(index)
    prefer_list[index]=prefers

for index in order:    
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.    
    prefer_candidates=get__prefer_candidates(prefer_list[index])
    if len(prefer_candidates)==1:
        x,y=prefer_candidates[0][0],prefer_candidates[0][1]
    
    # 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    else:
        empty_candidates=get_empty_candidates(prefer_candidates)
        if len(prefer_candidates)==1:
            x,y=empty_candidates[0][0],empty_candidates[0][1]
        
        # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        else:
            empty_candidates.sort()
            x,y=empty_candidates[0][0],empty_candidates[0][1]
    
    students[x][y]=index

print(get_satisfaction())
N, M = map(int, input().split())
matrix = []
ds_list=[]
answer=[0,0,0,0]

#상하좌우
dx=[None,-1,1,0,0]
dy=[None,0,0,-1,1]

for _ in range(N):
    matrix.append(list(map(int, input().split())))
for _ in range(M):
    d,s=map(int,input().split())
    ds_list.append((d,s)) #방향, 거리

shark_x,shark_y=N//2,N//2

value_arr=[] # 구슬값 배열
xyToIndex =[[-1]*N for _ in range(N)] # [x][y]가 arr의 몇번인지

x, y = N // 2, N // 2
value_arr.append(0) # 상어
xyToIndex[x][y]=len(value_arr)-1

for i in range(1,N):
    if i % 2==1: # 홀수
        for k in [3,2]:
            for j in range(i):
                x,y=x+dx[k],y+dy[k]
                value_arr.append(matrix[x][y])
                xyToIndex[x][y]=len(value_arr)-1
    else: # 짝수
        for k in [4,1]:
            for j in range(i):
                x,y=x+dx[k],y+dy[k]
                value_arr.append(matrix[x][y])
                xyToIndex[x][y] = len(value_arr) - 1

for _ in range(N-1):
    x,y=x+dx[3],y+dy[3]
    value_arr.append(matrix[x][y])
    xyToIndex[x][y]=len(value_arr)-1

#구슬 이동
def move_marble():
    global value_arr

    count=value_arr.count(-1)
    value_arr=[v for v in value_arr if v!=-1]
    value_arr.extend([0]*count)

    for mi in range(N):
        for mj in range(N):
            index=xyToIndex[mi][mj]
            matrix[mi][mj]=value_arr[index]

#구슬 폭발
def explode_marble():
    while True:
        total_exploded_count=0
        prev_value=value_arr[1]
        explode_list=[1]
        count = 1

        for i in range(2,len(value_arr)):
            if value_arr[i]!=0 and value_arr[i]==prev_value:
                count+=1
                explode_list.append(i)
            else:
                if count>=4:
                    if prev_value<4:
                        answer[prev_value]+=count
                    total_exploded_count+=count
                    for e in explode_list:
                        value_arr[e]=-1
                count=1
                prev_value=value_arr[i]
                explode_list=[i]

        if total_exploded_count==0:
            break
        move_marble()

#구슬 변화 : 구슬의 개수, 구슬의 번호
def update_marble():
    global value_arr
    new_arr=[0] #상어

    prev_value=value_arr[1]
    count=1
    for mi in range(2,len(value_arr)):
        if len(new_arr)>=N*N: # 전부 참
            break
        if value_arr[mi]==0:
            if prev_value>0:
                new_arr.append(count)
                new_arr.append(prev_value)
                prev_value=0
                break
        elif value_arr[mi]==prev_value:
            count+=1
        else:
            new_arr.append(count)
            new_arr.append(prev_value)
            prev_value=value_arr[mi]
            count=1

    if len(new_arr)<N*N and prev_value>0:
        new_arr.append(count)
        new_arr.append(prev_value)

    length=len(new_arr)
    for _ in range(length,N*N):
        new_arr.append(0)

    value_arr=new_arr
    for mi in range(N):
        for mj in range(N):
            matrix[mi][mj]=value_arr[xyToIndex[mi][mj]]


for i in range(M):
    d,s=ds_list[i]
    removed=0
    for j in range(1,s+1):
        break_x,break_y=shark_x+(j*dx[d]),shark_y+(j*dy[d])
        value_arr[xyToIndex[break_x][break_y]]=-1

    move_marble()
    explode_marble()
    update_marble()

print(answer[1]+2*answer[2]+3*answer[3])
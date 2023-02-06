# 다시 
n=5
build_frame=[
    [1,0,0,1],
    [1,1,1,1],
    [2,1,0,1],
    [2,2,1,1],
    [5,0,0,1],
    [5,1,0,1],
    [4,2,1,1],
    [3,2,1,1]
    ]

def print_wall(wall):
    for i in range(n+1):
        for j in range(n+1):
            print(wall[i][j],end=' ')
        print()

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

def is_column_valid(wall,x,y):
    return x==n or (y>0 and wall[x][y-1]==1) or wall[x+1][y]==0

def is_beam_valid(wall,x,y):
    print(x,y)
    return wall[x+1][y]==0 or wall[x+1][y+1]==0 or ((y>0 and wall[x][y-1]==1) and (y<n and wall[x][y+1]==1))

def solution(n, build_frame):
    answer = [[]]
    wall=[[-1]*(n+1) for _ in range(n+1)] # 0~5

    for x,y,a,b in build_frame:
        tmp=x
        x=n-y
        y=tmp

        print(x,y,a,b)
        if a==0:
            if b==1:
                if is_column_valid(wall,x,y): # 기둥 설치
                    wall[x][y]=0 
            else: # 기둥 삭제
                wall[x][y]=-1
                can_delete=True
                
                if wall[x+1][y]==0 and not is_column_valid(wall,x+1,y):
                    can_delete=False 
                if wall[x+1][y]==1 and not is_beam_valid(wall,x+1,y):
                    can_delete=False
                if y>0 and wall[x+1][y-1]==1 and not is_beam_valid(wall,x+1,y-1):
                    can_delete=False
                
                if not can_delete:
                    wall[x][y]=0
        else:
            if b==1:
                if is_beam_valid(wall,x,y): # 보 설치
                    wall[x][y]=1
            else: # 보 삭제
                wall[x][y]=-1
                can_delete=True
                
                if wall[x][y+1]==0 and not is_column_valid(wall,x,y+1):
                    can_delete=False 
                if wall[x][y+1]==1 and not is_beam_valid(wall,x,y+1):
                    can_delete=False
                if y<0 and wall[x][y-1]==1 and not is_beam_valid(wall,x,y-1):
                    can_delete=False
                
                if not can_delete:
                    wall[x][y]=1

    print_wall(wall)
    return answer

print(solution(n,build_frame))
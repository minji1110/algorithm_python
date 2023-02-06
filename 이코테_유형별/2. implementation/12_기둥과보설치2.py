# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
def is_valid_frame(frame):
    for x,y,a in frame:
        if a==0:
            valid = y==0 or [x,y,1] in frame or [x-1,y,1] in frame or [x,y-1,0] in frame
        else:
            valid= [x,y-1,0] in frame or [x+1,y-1,0] in frame or ([x-1,y,1] in frame and [x+1,y,1] in frame)
        if not valid:
            return False

    return True

# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
def solution(n, build_frame):
    answer = []

    for x,y,a,b in build_frame:
        if a==0:
            # 기둥 삭제
            if b==0:
                answer.remove([x,y,0])
                if not is_valid_frame(answer):
                    answer.append([x,y,0])
            # 기둥 설치
            else:
                answer.append([x,y,0])
                if not is_valid_frame(answer):
                    answer.remove([x,y,0])
        else:
            # 보 삭제
            if b==0:
                answer.remove([x,y,1])
                if not is_valid_frame(answer):
                    answer.append([x,y,1])
            # 보 설치
            else:
                answer.append([x,y,1])
                if not is_valid_frame(answer):
                    answer.remove([x,y,1])
    
    answer.sort()
    return answer

n=5
build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))

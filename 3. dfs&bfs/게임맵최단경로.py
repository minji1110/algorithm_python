# 프로그래머스

from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    q=deque()

    #동,서,남,북
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    now_x , now_y ,depth = 0,0,1
    visited[0][0]=True
    q.append((now_x,now_y,depth))

    flag = False
    while(q):
        now_x,now_y,depth = q.popleft()
         #도달
        if now_x == n-1 and now_y==m-1:
            answer=depth
            flag=True
            break

        for i in range(4):
            #동,서,남,북으로 이동
            next_x,next_y = now_x+dx[i], now_y+dy[i]
            if 0<=next_x<n and 0<=next_y<m: # 갈 수 있는 좌표
                 # 방문x, 벽x
                if not visited[next_x][next_y] and maps[next_x][next_y]!=0:
                    visited[next_x][next_y]=True
                    q.append((next_x,next_y,depth+1))
    
    if(not flag):
        answer = -1
    return answer


print(solution(maps))

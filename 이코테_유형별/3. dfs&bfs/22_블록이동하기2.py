from collections import deque

def solution(board):
    answer = 0
    n=len(board)

    visited=[]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    q=deque()
    q.append(({(0,0),(0,1)},0))
    visited.append({(0,0),(0,1)})

    while q:
        location,t=q.popleft()
        location=list(location)
        a,b,c,d=location[0][0],location[0][1],location[1][0],location[1][1]

        # 도착
        if a==b==n-1 or c==d==n-1:
            answer=t
            break

        # 상하좌우
        for i in range(4):
            na,nb=a+dx[i],b+dy[i]
            nc,nd=c+dx[i],d+dy[i]
            if 0<=na<n and 0<=nb<n and 0<=nc<n and 0<=nd<n and board[na][nb]==board[nc][nd]==0:
                next={(na,nb),(nc,nd)}
                if next not in visited:
                    q.append((next,t+1))
                    visited.append(next)
                
        # 회전 
        if a==c: 
            #가로->위회전
            if 0<=a-1<n and board[a-1][b]==board[a-1][d]==0:
                next1={(a-1,b),(a,b)}
                next2={(c-1,d),(c,d)}
                
                for next in next1,next2:
                    if next not in visited:
                        q.append((next,t+1))
                        visited.append(next)
            #가로->아래회전
            if 0<=a+1<n and board[a+1][b]==board[a+1][d]==0:
                next1={(a,b),(a+1,b)}
                next2={(c,d),(c+1,d)}

                for next in next1,next2:
                    if next not in visited:
                        q.append((next,t+1))
                        visited.append(next)
        else: 
            #세로->오른회전
            if 0<=b+1<n and board[a][b+1]==board[c][b+1]==0:
                next1={(a,b),(a,b+1)}
                next2={(c,d),(c,d+1)}
                
                for next in next1,next2:
                    if next not in visited:
                        q.append((next,t+1))
                        visited.append(next)
            #세로->왼회전
            if 0<=b-1<n and board[a][b-1]==board[c][b-1]==0:
                next1={(a,b-1),(a,b)}
                next2={(c,d-1),(c,d)}

                for next in next1,next2:
                    if next not in visited:
                        q.append((next,t+1))
                        visited.append(next)

    return answer

board=[
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]]	

print(solution(board))
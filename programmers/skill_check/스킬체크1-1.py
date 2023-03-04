def solution(board, moves):
    answer = 0
    n=len(board)

    stack=[-1]
    for move in moves:
        for i in range(n):
            if board[i][move-1]>0:
                no=board[i][move-1]
                if no==stack[-1]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(no)
                board[i][move-1]=0
                break
    
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves=[1,5,3,5,1,2,1,4]	
print(solution(board,moves))
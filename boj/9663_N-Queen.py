N=int(input())
answer=0

def is_valid(row):
    for k in range(row):
        # 같은 열 또는 같은 대각선
        if queens[k]==queens[row] or row-k == abs(queens[row]-queens[k]):
            return False
    return True


def nqueen(row): # row 번째 줄에 queen 놓음
    global answer
    if row==N:
        answer+=1
        return
    
    for i in range(N):
        queens[row]=i
        if is_valid(row):
            nqueen(row+1)

queens=[-1]*N
nqueen(0)
print(answer)
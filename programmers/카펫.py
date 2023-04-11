def solution(brown, yellow):
    answer = []
    total_count=brown+yellow
    
    col=3
    while True:
        if total_count%col==0:
            row=total_count//col
            b=2*(row+col)-4
            y=total_count-b
            
            print('row,col,b,y=',row,col,b,y)
            if b == brown and y==yellow:
                answer=[row,col]
                break
        col+=1
    return answer

brown,yellow=24,24
print(solution(brown,yellow))
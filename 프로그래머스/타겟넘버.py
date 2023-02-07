answer = 0

def dfs(numbers,target,index,total):
    global answer
    if index==len(numbers)-1:
        if total==target:
            answer+=1
        return 
    
    dfs(numbers,target,index+1,total+numbers[index+1])
    dfs(numbers,target,index+1,total-numbers[index+1])
    

def solution(numbers, target):
    global answer
    dfs(numbers,target,-1,0)
    return answer

numbers=[1, 1, 1, 1, 1]
target=3

print(solution(numbers,target))

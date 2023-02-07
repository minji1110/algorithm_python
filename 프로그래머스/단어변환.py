from collections import deque

def is_adjacent(w1,w2):
    diff=0
    length=len(w1)
    for i in range(length):
        if w1[i]==w2[i]:
            continue
        diff+=1
    return diff==1

def set_adjacent_list(words,adj_list):
    for i in range(len(words)):
        adj=[]
        for j in range(len(words)):
            if is_adjacent(words[i],words[j]):
                adj.append(j)
        adj_list.append(adj)

def solution(begin, target, words):
    if target not in words:
        return 0
    
    adj_list=[]
    set_adjacent_list(words,adj_list)

    answer = 0
    q=deque()
    visited=[False]*(len(words))
    
    for i in range(len(words)):
        if is_adjacent(begin, words[i]):
            visited[i]=True
            q.append((i,1))

    while q:
        index, cnt =q.popleft()
        if words[index]==target:
            answer=cnt
            break

        for next in adj_list[index]:
            if not visited[next]:
                visited[next]=True
                q.append((next, cnt+1))

    return answer

words=["hot", "dot", "dog", "lot", "log", "cog"]
begin="hit"
target="cog"
print(solution(begin,target,words))
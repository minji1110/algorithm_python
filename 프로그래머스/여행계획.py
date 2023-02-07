def dfs(tickets,used,i,cnt,route):
    
    ticket=tickets[i]
    route.append(ticket[1]) # 도착지 저장
    used[i]=True   

    if cnt==len(tickets):
        return True
     
    for t in range(len(tickets)):
        if not used[t] and ticket[1]==tickets[t][0]:
            result = dfs(tickets,used,t,cnt+1,route)
            if(result):
                return True
            route.pop()
            used[t]=False
    return False

def solution(tickets):
    answer = []
    n=len(tickets)
    used=[False]*n
    
    tickets.sort()
    for i in range(n):
        if tickets[i][0]=="ICN":
            route=["ICN"]
            dfs(tickets,used,i,1,route)
            if len(route)==n+1:
                answer=route
                break
            used[i]=False
    
    return answer

tickets=[["ICN", "JFK"], ["HND", "IAD"],["JFK","ABC"] ,["JFK", "HND"],["IAD","JFK"]]
# tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
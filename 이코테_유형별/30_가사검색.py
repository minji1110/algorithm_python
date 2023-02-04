from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    words_by_len=[[] for _ in range(10001)]
    words_by_len_rev=[[] for _ in range(10001)]

    words.sort()
    for word in words:
        words_by_len[len(word)].append(word)
    
    for i in range(len(words)):
        words[i]=words[i][::-1]
    
    words.sort()
    for word in words:
        words_by_len_rev[len(word)].append(word)

    for q in queries:
        if q[0]=='?':
            q=q[::-1]
            arr=words_by_len_rev[len(q)]
        else:
            arr=words_by_len[len(q)]
        
        left=bisect_left(arr,q)
        q=q.replace('?','z')
        right=bisect_right(arr,q)

        answer.append(right-left)
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))
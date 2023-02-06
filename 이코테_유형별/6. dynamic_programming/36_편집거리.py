A=input()
B=input()

def insert(edited_list,next_edited_list):
    for i in range(len(edited_list)):
        before = edited_list[i]
        for j in range(len(before)+1):
            for k in range(26):
                alpha = chr(ord('a')+k)
                inserted = before[0:j] +alpha+before[j:]
                if inserted==B:
                    return True
                next_edited_list.append(inserted)
    return False

def remove(edited_list,next_edited_list): 
    for i in range(len(edited_list)):
        before=edited_list[i]
        for j in range(len(before)):
            removed = before[0:j]+before[j+1:]
            if removed==B:
                return True
            next_edited_list.append(removed)
    return False

def replace(edited_list,next_edited_list):
    for i in range(len(edited_list)):
        before=edited_list[i]
        for j in range(len(before)):
            for k in range(26):
                alpha = chr(ord('a')+k)
                if alpha!=before[j]:
                    replaced=list(before)
                    replaced[j]=alpha
                    replaced=''.join(replaced)
                    if replaced==B:
                        return True
                    next_edited_list.append(replaced)
    return False


answer=1
edited_list=[]
edited_list.append(A)

while(True):
    next_edited_list=[]
    step1=insert(edited_list,next_edited_list)
    step2=remove(edited_list,next_edited_list)
    step3=replace(edited_list,next_edited_list)

    if not step1 and not step2 and not step3:
        edited_list=list(set(next_edited_list)) # 중복 제거
        answer+=1
    else:
        break

print(answer)


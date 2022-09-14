# 재귀함수를 이용한 bs
def binary_search_recall(array, target, start, end):
    if start>end:
        return -1
    else :
        mid = (start+end) // 2
        if array[mid] == target: 
            return mid
        elif array[mid]<target:
            return binary_search_recall(array, target, mid+1, end)
        else:
            return binary_search_recall(array,target,start,mid-1)


# 반복문을 이용한 bs
def binary_search_while(array, target, start, end):
    while(start<=end):
        mid=(start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1

# main
array=list(map(int, input('정렬된 배열을 입력하세요 : ').split()))
target=int(input('찾을 숫자를 입력하세요 : '))

result_recall = binary_search_recall(array, target, 0, len(array)-1)
result_while=binary_search_while(array,target,0,len(array)-1)

if result_recall == -1 : print('찾는 원소가 없습니다.')
else : print(result_recall+1,'번째 원소입니다.')

if result_while == -1 : print('찾는 원소가 없습니다.')
else : print(result_while+1,'번째 원소입니다.')



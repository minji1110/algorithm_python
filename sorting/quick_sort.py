# 퀵 정렬
# pivot 을 제일 앞 원소로 두고, 나머지를 pivot 이하 초과로 분리
# pivot 이하 리스트 + pivot + pivot 초과 리스트 로 전체 리스트 유지
# O(NlogN)

def quick_sort(arr):
    if len(arr)<=1 :
        return arr
    
    pivot=arr[0]
    tail= arr[1:]   # pivot 제외 정렬 대상

    under_pivot = [i for i in tail if i<=pivot]
    over_pivot = [i for i in tail if i>pivot]

    return quick_sort(under_pivot) + [pivot] + quick_sort(over_pivot)

arr=[3,2,1,6,5,4,9,8,7]
print(quick_sort(arr))
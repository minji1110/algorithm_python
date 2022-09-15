# 삽입정렬
# 두번째 원소부터 시작, 적절한 위치에 삽입 (자신인덱스-1 부터 살펴보며 자신보다 크면 swap)
# O(N^2)

arr=[3,2,1,6,5,4,9,8,7]

for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break   # 내 왼쪽이 더 작은경우 stop

print(arr)
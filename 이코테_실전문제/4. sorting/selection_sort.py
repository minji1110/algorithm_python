# 선택정렬
# 배열에서 가장 작은 값 골라 맨 앞 데이터와 교체 : i번째 단계에서는 가장 작은 값을 i-1 번째 수와 교체
# O(n^2)

arr=[3,2,1,6,5,4,9,8,7]

for i in range(len(arr)):
    min_index = i   # 최소값 찾기
    for j in range(i+1, len(arr)): 
        if(arr[min_index]>arr[j]):
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i] #swap

print(arr)


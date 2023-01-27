# 계수 정렬
# 데이터의 최대값(k) 크기의 리스트 생성, n개의 데이터에 대해 해당 데이터 위치의 리스트값 ++
# 모든 데이터가 자연수이고 , 데이터 수 많이 크지 않고, 중복이 많을 때 유리!!
# O(n+k) : n번 돌며 리스트에 넣고, k번 돌며 출력

arr=[3,3,2,1,6,5,5,4,9,8,7,7] #모든 데이터가 자연수, 최대값 9로 작음

count_arr=[0]*(max(arr)+1)

for i in arr:
    count_arr[i]+=1

for i in range(len(count_arr)):
    for j in range(count_arr[i]):
        print(i, end=" ")

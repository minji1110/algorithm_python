# 계수 정렬
# 데이터의 수(n) 크기의 리스트 생성, 해당 데이터 위치의 리스트값 ++
# 모든 데이터가 자연수이고 , 데이터 수 많이 크지 않고, 중복이 많을 때 유리!!

arr=[3,3,2,1,6,5,5,4,9,8,7,7] #모든 데이터가 자연수, 최대값 9로 작음

count_arr=[0]*(max(arr)+1)

for i in arr:
    count_arr[i]+=1

for i in range(len(count_arr)):
    for j in range(count_arr[i]):
        print(i, end=" ")

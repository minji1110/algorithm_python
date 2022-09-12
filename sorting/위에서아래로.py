n=int(input())

arr=[]
for i in range(n):
    arr.append(int(input()))

arr.sort()
arr.reverse

for i in arr:
    print(i, end=" ")

def setting(arr):
    return arr[1]

n=int(input())

students=[]
for i in range(n):
    name, score = input().split()
    students.append((name,score))

students.sort(key=setting)

for stu in students:
    print(stu[0], end=" ")
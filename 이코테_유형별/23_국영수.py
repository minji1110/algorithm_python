import sys
def input(): return sys.stdin.readline().rstrip()

students=[]
N=int(input())
for i in range(N):
    name,korean,english,math=input().split()
    korean=int(korean)
    english=int(english)
    math=int(math)

    students.append((-korean,english,-math,name))
students.sort()

for student in students:
    print(student[3])

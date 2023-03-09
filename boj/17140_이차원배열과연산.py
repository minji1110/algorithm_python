import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

data=[[0]*100 for _ in range(100)]
r,c,k=map(int,input().split())
r_len,c_len=3,3

for i in range(3):
    x,y,z=map(int,input().split())
    data[i][0],data[i][1],data[i][2]=x,y,z

#r연산
def r_calculation():
    global data,r_len,c_len
    max_c_len=0

    for i in range(r_len):
        exist_nums=[]
        cnt_list=[0]*101 #1~99까지 수의 등장횟수
        
        row=data[i]
        for j in range(c_len):
            num=row[j]
            if num==0:
                continue
            if num not in exist_nums:
                exist_nums.append(num)
            cnt_list[num]+=1
        
        pq=[]
        for num in exist_nums:
            heapq.heappush(pq,(cnt_list[num],num))
        
        data[i]=[]
        while pq:
            cnt,num=heapq.heappop(pq)
            data[i].append(num)
            data[i].append(cnt)
            
            if len(data[i])==100:
                break
        max_c_len=max(max_c_len,len(data[i]))

        # 0 채우기
        row_len=len(data[i])
        for _ in range(row_len,100):
            data[i].append(0)
    
    c_len=max_c_len

#c연산
def c_calculation():
    global data,r_len,c_len
    max_r_len=0

    for i in range(c_len):
        exist_nums=[]
        cnt_list=[0]*101

        for row in range(r_len):
            num=data[row][i]
            if num==0:
                continue
            if num not in exist_nums:
                exist_nums.append(num)
            cnt_list[num]+=1
        
        pq=[]
        for num in exist_nums:
            heapq.heappush(pq,(cnt_list[num],num))
        
        row_num=0
        while pq:
            cnt,num=heapq.heappop(pq)
            data[row_num][i]=num
            data[row_num+1][i]=cnt

            row_num+=2
            max_r_len=max(max_r_len,row_num)
            
            if row_num==100:
                break
        
        # 0채우기
        for z in range(row_num,100):
            data[z][i]=0
    
    r_len=max_r_len

# def print_data():
#     global data,r_len,c_len

#     print(f"rlen={r_len}, clen={c_len}")
#     for i in range(r_len):
#         for j in range(c_len):
#             print(data[i][j],end=" ")
#         print()

t=0
while True:

    if data[r-1][c-1]==k:
        print(t)
        break

    if r_len>=c_len:
        # print('======R======')
        r_calculation()
        # print_data()
    else:
        # print('======C======')
        c_calculation()
        # print_data()
    
    t+=1
    if t==100:
        print(-1)
        break
num=list(map(int,input()))
cnt_list=[0,0]

now=-1
for i in num:
    if i==now:
        continue
    now=i
    cnt_list[now]+=1

print(min(cnt_list))



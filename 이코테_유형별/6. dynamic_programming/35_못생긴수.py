def is_ugly_number(x):
    if x==1:
        return True
    while x%5==0:
        x//=5
        if x==1:
            return True
    while x%3==0:
        x//=3
        if x==1:
            return True
    while x%2==0:
        x//=2
        if x==1:
            return True
    return False

n=int(input())
cnt=0
now_x=1

while True:
    if is_ugly_number(now_x):
        cnt+=1
    if cnt==n:
        break
    now_x+=1

print(now_x)
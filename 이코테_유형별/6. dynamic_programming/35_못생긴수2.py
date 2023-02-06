n=int(input())

ugly_number=[0]*n
ugly_number[0]=1

prime2=2
prime3=3
prime5=5
i2=i3=i5=1

for i in range(1,n):
    un = min(prime2,prime3,prime5)
    ugly_number[i] = un

    if ugly_number[i] == prime2:
        prime2=2*ugly_number[i2]
        i2+=1
    
    if ugly_number[i]==prime3:
        prime3=3*ugly_number[i3]
        i3+=1
    
    if ugly_number[i]==prime5:
        prime5=5*ugly_number[i5]
        i5+=1
    
print(ugly_number[n-1])
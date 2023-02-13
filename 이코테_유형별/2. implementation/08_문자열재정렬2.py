s=list(input())
s.sort()

alpha_start_index=len(s)
for i in range(len(s)):
    if s[i].isalpha():
        alpha_start_index=i
        break

num_list=s[:alpha_start_index]
alpha_list=s[alpha_start_index:]

nums=0
for num in num_list:
    nums+=int(num)

print(''.join(alpha_list)+str(nums))
from itertools import permutations
import math

def is_prime(number):
    if number==1:
        return False
    for i in range(2,int(math.sqrt(number)+1)):
        if number%i==0:
            return False
    return True
    
def solution(numbers):
    answer = 0
    numbers=list(numbers)
    
    for length in range(1,len(numbers)+1):
        for candidate in set(list(permutations(numbers,length))):
            print(f'candidate={candidate}')
            if candidate[0]=='0': # 가장 앞이 0인경우 무시
                continue
            
            number=int(''.join(candidate))
            if is_prime(number):
                answer+=1
    return answer

numbers="999"
print(solution(numbers))
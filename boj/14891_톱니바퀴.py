import sys
def input() : return sys.stdin.readline().rstrip()

def rotate_clockwise(wheel):
    return wheel[7:]+wheel[:7]

def rotate_anticlockwise(wheel):
    return wheel[1:]+wheel[0:1]

wheels=[[-1]*8]
for _ in range(4):
    wheels.append(list(map(int,input())))

k=int(input())
for _ in range(k):
    rot_index, rot_direction = map(int,input().split()) #회전 번호, 회전 방향

    #왼쪽 검사
    now=rot_index
    prev_rot_direction=rot_direction
    tmp=wheels[now][6]
    while(now>1):
        left=now-1
        
        if tmp!=wheels[left][2]:
            tmp=wheels[left][6]
            if prev_rot_direction==1:
                wheels[left]=rotate_anticlockwise(wheels[left])
                prev_rot_direction=-1
            else:
                wheels[left]=rotate_clockwise(wheels[left])
                prev_rot_direction=1
            now=left
        else:
            break
    
    #오른쪽 검사
    now=rot_index
    prev_rot_direction=rot_direction
    tmp=wheels[now][2]
    while(now<4):
        right=now+1

        if tmp!=wheels[right][6]:
            tmp=wheels[right][2]
            if prev_rot_direction==1:
                wheels[right]=rotate_anticlockwise(wheels[right])
                prev_rot_direction=-1
            else:
                wheels[right]=rotate_clockwise(wheels[right])
                prev_rot_direction=1
            now=right
        else:
            break
    
    if rot_direction==1:
        wheels[rot_index]=rotate_clockwise(wheels[rot_index])
    else:
        wheels[rot_index]=rotate_anticlockwise(wheels[rot_index])
    
score=0
for i in range(1,5):
    if wheels[i][0]==1:
        score+=(2**(i-1))
print(score)
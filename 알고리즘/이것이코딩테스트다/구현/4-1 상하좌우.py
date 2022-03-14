#상하좌우

n = int(input())
m = list(input().split())
now =[1,1]

for i in m:
    if i == 'R' and 0 < now[1]+1 <= 100:
        now[1] += 1
    if i == 'L' and 0 < now[1]-1 <= 100:
        now[1] -= 1
    if i == 'U' and 0 < now[0]-1 <= 100:
        now[0] -= 1
    if i == 'D' and 0 < now[0]+1 <= 100:
        now[0] += 1
        
print(now[0],now[1])

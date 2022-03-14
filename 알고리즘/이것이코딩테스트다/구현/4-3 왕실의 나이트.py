# 왕실의 나이트

n  = input()
x = n[0]

# int(ord(n[0])-ord('a')) + 1

if x =='a':
    x = 1
elif x == 'b':
    x = 2
elif x =='c':
    x = 3
elif x =='d':
    x = 4
elif x == 'e':
    x=5
elif x == 'f':
    x=6
elif x == 'g':
    x=7
elif x == 'h':
    x=8
y = int(n[1])

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]


count = 0
for i in range(8):
    nx = dx[i] + x
    ny = dy[i] + y
    if nx > 8 or nx < 1 or ny > 8 or ny < 1:
        continue
    count +=1

print(count)

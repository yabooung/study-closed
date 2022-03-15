# 게임개발

n, m = map(int,input().split())

d = [[0] * n for _ in range(m)]
char = list(map(int,input().split()))
jido = list()
for i in range(m):
    jido.append(list(map(int, input().split() )))

def turn_left():
    char[2] -= 1
    if char[2] == -1:
        char[2] = 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
jido[char[0]][char[1]] = 1
all_turn = 0
count = 1
while 1:

    turn_left()
    all_turn += 1
    nx = char[0] + dx[char[2]]
    ny = char[1] + dy[char[2]]
    if d[nx][ny] == 0 and jido[nx][ny] == 0:
        d[nx][ny] = 1
        char[0], char[1] = nx, ny
        count += 1
        all_turn = 0
    elif d[nx][ny] == 1 or jido[nx][ny] == 1:
        d[nx][ny] = 1


    if all_turn == 4:
        nx = char[0] - dx[char[2]]
        ny = char[1] = dy[char[2]]
        if n < nx or nx < 0 or m < ny or ny < 0:
            break
        if d[nx][ny] == 0 and jido[nx][ny] == 0 :
            char[0], char[1] == nx, ny
            all_turn = 0
            count += 1
        else:
            break
print(count)

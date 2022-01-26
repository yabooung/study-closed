#1018. 체스판 다시 칠하기
#브루트포스 모든 경우의 수 구하기

n, m = map(int,input().split())
lst = []
for i in range(n):
    lst.append(input())

cnt_lst = []
for y in range(n-7):
    for x in range(m-7):
        cnt = 0
        cnt_2 = 0
        # if lst[y][x] =='W': # 맨왼쪽위가 'W'일 경우와 'B'일 경우를 나눴는데, 안되는 경우가 있어서 그냥 다 구하기로 했다.
        for j in range(y,y+8,2):
            for i in range(x,x+8,2):
                if lst[j][i] != 'W':
                    cnt += 1
                if lst[j][i+1] != 'B':
                    cnt += 1
                if lst[j+1][i] != 'B':
                    cnt += 1
                if lst[j+1][i+1] != 'W':
                    cnt += 1
        cnt_lst.append(cnt)
        # elif lst[y][x] =='B':
        for j in range(y,y+8,2):
            for i in range(x,x+8,2):
                if lst[j][i] != 'B':
                    cnt_2 += 1
                if lst[j][i+1] != 'W':
                    cnt_2 += 1
                if lst[j+1][i] != 'W':
                    cnt_2 += 1
                if lst[j+1][i+1] != 'B':
                    cnt_2+= 1
        cnt_lst.append(cnt_2)

print(min(cnt_lst))

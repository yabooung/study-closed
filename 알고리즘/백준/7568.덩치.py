# 7568.덩치
# 숫자가작기때문에(50) 전체검색으로 품
t = int(input())
n = []
ans = []
for tc in range(t):
    n.append(list(map(int, input().split())))

for i in range(t):
    count = 1
    for j in range(t):
        if n[i][0] < n[j][0] and n[i][1] < n[j][1]:
            count += 1
    ans.append(count)
for i in ans:
    print(i,end=' ')

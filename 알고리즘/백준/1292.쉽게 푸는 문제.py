#1292. 쉽게 푸는 문제
n, m = map(int,input().split())
num = 1
lst = []
cnt = num
now = 1

while num <= m:
    cnt = num
    if now < cnt:
        lst.append(num)
        now += 1
    elif now == cnt:
        lst.append(num)
        now = 1
        num += 1
ans = 0
for i in range(n-1,m):
    ans += lst[i]
print(ans)

#1654. 랜선 자르기
#이분탐색
#이분탐색 개념학습하기

n,m = map(int,input().split())
lst = []
total = 0
for i in range(n):
    k = int(input())
    lst.append(k)
    total += k

i = 0
ans = 0
end = max(lst)
start = 1
while start <= end:
    mid = (start + end) // 2
    while i < n:
        ans += lst[i] // mid
        i += 1
    i = 0
    if ans >= m:
        start = mid + 1
    else:
        end = mid - 1
    ans = 0

print(end)

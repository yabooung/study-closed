n, m = map(int, input().split())

result = 0
for i in range(n):
    lst = list(map(int,input().split()))
    min_n = 10001
    for j in range(m): # 현재 줄에서 작은 수 찾기
        if min_n > lst[j]:
            min_n = lst[j]
    if result < min_n: # 작은 수 끼리의 값 비교하기
        result = min_n
print(result)



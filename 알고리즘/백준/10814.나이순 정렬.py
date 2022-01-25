#10814. 나이순 정렬
# 10초 걸림

n = int(input())
m = ['']*n
for i in range(n):
    m[i] = list(map(str,input().split()))

i = 0
age = 1

while m:
    if m[i][0] == str(age):
        print(f'{m[i][0]} {m[i][1]}')
        m.pop(i)
    else:
        i += 1
    if i == len(m):
        i = 0
        age += 1

    if age == 201:
        break

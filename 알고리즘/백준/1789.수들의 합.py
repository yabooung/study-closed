#백준 1789 수들의 합
#이진탐색

k = 0
arrow = int(input())
n = 0
while k < arrow:
    n += 1
    k += n
    if n >= arrow -k:
        break
print(k,n)
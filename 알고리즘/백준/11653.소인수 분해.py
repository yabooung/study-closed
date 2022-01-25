#백준 11653 소인수분해
n = int(input())
k = 2
count = 0
while n >= k:
    if n % k != 0:
        k += 1
    if n % k == 0:
        n = n // k
        print(k)
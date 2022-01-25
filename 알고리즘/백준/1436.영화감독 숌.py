#1436 영화감독 숌
#완전탐색
#숫자가 10000까지 허용되기 때문에 완전탐색으로 풀었고
#10000을 넣으면 1.~초가 나온다
t = int(input())
n = 1
cnt = 0
while n:
    n += 1
    k = str(n)
    if k.find('666') != -1:
        cnt += 1
    if cnt == t:
        break
print(n)

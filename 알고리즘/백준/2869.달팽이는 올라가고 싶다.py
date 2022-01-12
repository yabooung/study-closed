# 2869. 달팽이는 올라가고 싶다
# 정수와 실수 판별한는 방법
# is_integer() 백준에서는 안됌
a, b, v = map(int, input().split())
if a == v:
    cnt =0
else:
    cnt = (v-a) / (a-b)
if cnt-int(cnt) != 0:
    cnt += 1
print(int(cnt)+1)

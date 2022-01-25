# 백준 1934 최소공배수

# 유클리드 호제법을 이용
# 최대 공약수 구하기
# x,y의 최대공약수는 y,r의 최대 공약수와 같다(x%y=r)
# 나머지의 값이 0이 될 때까지 나누어 주면 됌
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x
#최소 공배수 구하기 x*y 를 최대공약수로 나눈 몫이 최소공배수이다
def lcm(x,y):
    return int((x*y)/gcd(x,y))

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    print(lcm(n,m))

# 2609. 최대공약수와 최소공배수
# 유클리드 호제법을 쓰면 된다

def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
def lcm(a,b,c):
    return a*b //c
    
a, b = map(int,input().split())
print(Euclidean(a,b))
print(lcm(a,b,Euclidean(a,b)))

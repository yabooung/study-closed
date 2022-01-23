#백준 11557번 Yangjojang of The Year
#값을 뒤집어서 사용해보기
#딕셔너리 키로 int도 사용할 수 있다.

t = int(input())
for tc in range(t):
    dic = {}
    n = int(input())
    for i in range(n):
        university, drink = map(str, input().split())
        dic[int(drink)] = university
    print(dic.get(max(dic.keys())))

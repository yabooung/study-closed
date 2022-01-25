#4153. 직각삼각형
while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0] ** 2
    b = lst[1] ** 2
    c = lst[2] ** 2

    if a == 0 & b== 0 & c== 0:
        break
    else:
        # print(lst)
        if a + b == c:
            print('right')
        else:
            print('wrong')

# 백준 10214 Baseball
t = int(input())
for tc in range(t):
    y_score, k_score = 0, 0
    for i in range(9):
        y , k = list(map(int, input().split()))
        y_score += y
        k_score += k
    if y_score > k_score:
        print('Yonsei')
    elif y_score < k_score:
        print('Korea')
    else:
        print('Draw')

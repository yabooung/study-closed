# 1259. 팰린드롬수
t = True
while t:
    k = input()
    cnt = 0
    if k == '0':
        t = False
    else:
        for i in range(len(k)):
            if k[i] != k[-1-i]:
                print('no')
                break
            else:
                cnt += 1
        if cnt == len(k):
            print('yes')

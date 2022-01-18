# 2839. 설탕배달
# 그리디로 큰 수로 나누어지는게 가장 작은 값이고, 큰 수를 하나씩 줄여가면서 그 자리를 작은 수로 채운다.
big = 0
sugar = int(input())
if sugar == 0: #0일 경우 -1
    print('-1')
else:
    original = sugar
    lst = [-1] #기본 값 -1 넣어줌
    if sugar //5 == sugar / 5: #5로 나누어지고 몫이 자연수일 경우
        lst.append(sugar//5) #5로 나눈 것이 결과값이다
    else:
        for i in range(sugar//3): #3으로 나눴을 때 보다 적은 횟수만큼 해보면 된다.
            sugar = sugar - 5 # 하나씩 카운트 해준다
            if sugar < 0: # 답이 없는 경우라서 -1
                break
            big += 1
            small = 0
            if sugar // 3 == sugar / 3: #몫이 3으로 나눠지는 자연수일때
                small = sugar //3
                if 5*big + small*3 == original: #전체 값이 나누어지면 정답이다
                    lst.append(big+small)
    if original //3 == original /3: # 위에 경우로 나눠지지 않고 3으로 나누어지면 그게 값이다
        lst.append(original//3)
    if len(lst) == 1: # 나눠지지 않는다면 그대로 -1
        print(lst[0])
    else:
        lst.pop(0)
        print(min(lst)) # -1을 빼고 제일 작은 

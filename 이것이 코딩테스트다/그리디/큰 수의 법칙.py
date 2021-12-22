#import sys
# import time
# start = time.time()
#sys.stdin = open('input.txt', 'r', encoding='utf8')
#input = sys.stdin.readline

n, m, k = map(int,input().split())
data = list(map(int,input().split()))

# 정렬해서 큰 수를 k번 더하고 그 다음 수를 1번 더하고 다시 큰 수를 k번 더하면 된다. 이 것을 m번 될때까지 하면 된다.
data.sort(reverse=True) # 큰 수대로 정렬해준다.
first = data[0] #가장 큰 수를 뽑고
second = data[1] #그 다음 수를 뽑는다

answer = 0
while m > 0: #m 번만큼 수를 더한다
    count = k
    while count > 0: #k번 만큼 가장 큰 수를 더한다
        answer += first
        count -= 1
        m -= 1
        if m == 0: #m번 다 더할 경우 푼다
            break
    if m == 0:
        break
    answer += second
    m -= 1
print(answer)
# print(f'time: {time.time()-start:5f}')

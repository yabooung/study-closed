# 시각
#100000 안되면 문자열 연산으로 풀기 가능

n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k)+str(j)+str(i):
                count+=1
print(count)

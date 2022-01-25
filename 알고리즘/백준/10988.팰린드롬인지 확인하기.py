#백준 10988 팰린드롬인지 확인하기
# 여러가지 방법이 있다.
k = input()
reverse_k = ''
for i in range(len(k),0,-1):
    reverse_k = ''.join([reverse_k,k[i-1]])
if k == reverse_k:
    print(1)
else:
    print(0)

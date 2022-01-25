# 10828. 스택
# 백준에서 readline 안쓰면 시간초과가 뜬다
import sys
input = sys.stdin.readline
def stack(command,value='' ):
    if command == 'push':
        lst.append(value)
    elif command == 'pop':
        if lst:
            print(lst.pop(-1))
        else:
            print(-1)
    elif command == 'size':
        print(len(lst))
    elif command == 'empty':
        if not lst:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if lst:
            print(lst[len(lst)-1])
        else:
            print(-1)


lst=[]
n = int(input())
for tc in range(n):
    command = input().split()
    if len(command) == 2:
        stack(command[0],command[1])
    else:
        stack(command[0])

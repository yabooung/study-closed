#백준 1316 그룹단어체커

def str_count(x): 
    return ord(x)-97

tc = int(input())
count = 0
for t in range(tc):
    title = input().rstrip()
    lst = [1] * 26
    k = ''
    for i in range(len(title)):
        if title[i] == k:
            continue
        elif lst[(str_count(title[i]))] == 0:
            correct =0
            break
        lst[str_count(title[i])] = 0
        k = title[i]
        correct = 1
    if correct == 1:
        count += 1

print(count)
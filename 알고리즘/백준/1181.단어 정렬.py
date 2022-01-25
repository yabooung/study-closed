#1181. 단어 정렬

n = int(input())
lst = set() #세트로 받아서 중복되는 단어를 없애준다
lst_num = [0]*n

for i in range(n):
    k = input()
    lst.add(k)
arr = list(lst)
arr.sort()
i = 0 #인덱스 돌리기
lens = 1 #단어의 길이
box = [] #출력할 리스트
while len(arr)>0:
    if len(arr[i]) == lens: #단어의 길이가 짧으면 box로 보내고 리스트에서 없앤다.
        box.append(arr[i])
        arr.pop(i)
        i -= 1
    i += 1
    if i == len(arr): # 한 바퀴를 다 돌면 box에 있는 값들을 다 꺼낸다
        i = 0
        a = 0
        while a<len(box):
            print(box[a])
            a += 1
        box = [] 
        lens += 1 #box를 비우고 단어 숫자를 하나 늘려서 찾는다.

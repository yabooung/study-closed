# 2447 별 찍기 - 10
# 재귀로 푸는 문제 헷갈린다
def star(x,lst):
    ans = []
    if x == 3:
        return lst
    else:
        for i in lst:
            ans.append(i*3)
        for i in lst:
            ans.append(i+' '*len(lst)+i)
        for i in lst:
            ans.append(i*3)
        return star(x//3,ans)

lst =['***','* *','***']
n = int(input())
for i in star(n,lst):
    print(i)

#백준 1011 Fly me to the Alpha Centauri
#규칙을 찾아야 하는 문제이다

tc = int(input())
for t in range(tc):
    x, y = map(int,input().split())
    count =  0#총 이동횟수
    counts_count = 1 # count만큼 이동할 수 있는 거리의 갯수
    distance = y-x # 가야할 거리
    move_count = 0 #이동한 거리의 길이

    while distance> move_count: #간 거리가 남아있을 때
        count += 1 #이동을 하고
        move_count += counts_count #이동한 거리의 길이는 이동한 횟수만큼 더해준다.
        if count % 2 == 0: #이동횟수가 2의 배수라면 이동할 수 있는 거리의 횟수가 늘어난다
            counts_count += 1
    print(count)
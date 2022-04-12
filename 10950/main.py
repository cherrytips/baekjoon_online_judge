T = int(input())
case = []

for i in range(T):
    case.append(list(map(int, input().split())))

for i in range(len(case)):
    print(case[i][0]+case[i][1])

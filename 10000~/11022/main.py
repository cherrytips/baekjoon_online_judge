T = int(input())
case = []

for i in range(T):
    case.append(list(map(int, input().split())))

for i in range(T):
    print(
        f'Case #{i+1}: {case[i][0]} + {case[i][1]} = {case[i][0]+case[i][1]}')

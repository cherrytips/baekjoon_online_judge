def avg(list):
    result = 0
    for i in list:
        result += int(i)
    return result/len(list)


C = int(input())
for c in range(C):
    case = input().split(' ')
    N = case.pop(0)
    average = avg(case)
    count = 0

    for i in case:
        if int(i) > average:
            count += 1

    print(f'{count/len(case)*100:.3f}%')

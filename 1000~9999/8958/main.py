N = int(input())
for i in range(N):
    case = list(input())
    score = 0
    count = 0
    for j in case:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)

T = int(input())

for t in range(T):
    R, S = input().split(' ')

    result = ''
    for s in S:
        result += int(R)*s
    print(result)

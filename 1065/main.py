def hansu(num):
    num = list(str(num))
    for i in range(len(num)):
        num[i] = int(num[i])

    if len(num) == 1 or len(num) == 2:
        return True
    else:
        diff = num[1]-num[0]
        for i in range(1, len(num)-1):
            if num[i+1]-num[i] != diff:
                return False
        return True


N = int(input())
result = 0

for i in range(1, N+1):
    if hansu(i):
        result += 1

print(result)

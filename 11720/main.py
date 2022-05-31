N = int(input())
number = list(map(int, list(input())))
result = 0

for i in range(N):
    result += number[i]

print(result)

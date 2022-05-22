n = 0
answer = 0

for i in range(9):
    temp = int(input())
    if temp > n:
        n = temp
        answer = i+1

print(n)
print(answer)

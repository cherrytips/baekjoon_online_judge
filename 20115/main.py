N = int(input())
drink = list(map(int, input().split()))

drink.sort()
answer = drink[N-1]

for d in drink[:-1]:
  answer += d/2

print(answer)

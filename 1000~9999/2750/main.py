N = int(input())
result = []

for _ in range(N):
  result.append(int(input()))

result.sort()

for r in result:
  print(r)

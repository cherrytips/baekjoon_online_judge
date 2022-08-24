N = int(input())
P = list(map(int, input().split()))
result = 0

P.sort()

for n in range(N):
  result += sum(P)
  P.pop()

print(result)

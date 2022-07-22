N = int(input())
result = -1

for i in range(N):
  A, B = map(int, input().split())
  if A < B and (result > B or result == -1):
    result = B

print(result)

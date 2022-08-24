X = int(input())
N = int(input())

for n in range(N):
  a, b = map(int, input().split())
  X -= (a*b)

if X == 0:
  print('Yes')
else:
  print('No')

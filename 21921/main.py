N, X = map(int, input().split())
visits = list(map(int, input().split()))
answer = 0
max = 0

for i in range(N-X+1):
  cnt = sum(visits[i:i+X])
  if max < cnt:
    answer = 1
    max = cnt
  elif cnt != 0 and max == cnt:
    answer += 1

if max == 0:
  print('SAD')
else:
  print(max)
  print(answer)

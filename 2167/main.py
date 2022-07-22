N, M = map(int, input().split())
arr = []
answer = []

for i in range(N):
  temp_arr = list(map(int, (input().split())))
  arr.append(temp_arr)

K = int(input())

for i in range(K):
  i, j, x, y = map(int, input().split())
  result = 0

  for m in range(i-1, x):
    for n in range(j-1, y):
      result += arr[m][n]

  answer.append(result)

for a in answer:
  print(a)

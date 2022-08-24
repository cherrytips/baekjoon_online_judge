N, M = map(int, input().split())
A = list(map(int, input().split()))
count = 0
temp = 0
back = 0

for i in range(N):
  while back < N and temp < M:
    temp += A[back]
    back += 1
  if temp == M:
    count += 1
  temp -= A[i]

print(count)

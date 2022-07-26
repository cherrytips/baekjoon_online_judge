N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for i in range(N)]
answer = 0

D.sort()
D = list(reversed(D))

for i in range(N+1):
  cost = A+B*i
  calorie = C+sum(D[:i])

  per_one = calorie//cost

  if answer < per_one:
    answer = per_one

print(answer)

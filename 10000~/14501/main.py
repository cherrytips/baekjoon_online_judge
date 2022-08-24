N = int(input())
T = []
P = []
answer = 0

for i in range(N):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

for i in range(T[0]):
  money = 0
  day = i

  while day < N and day+T[day] <= N:
    money += P[day]
    day += T[day]

  if answer < money:
    answer = money

print(answer)

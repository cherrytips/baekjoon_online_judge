N = int(input())
people = []
result = []

for i in range(N):
  x, y = map(int, input().split())
  people.append([x, y])

for i in range(N):
  rank = 1
  for j in range(N):
    if i == j:
      continue
    elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
      rank += 1
  result.append(rank)

for r in result:
  print(r)

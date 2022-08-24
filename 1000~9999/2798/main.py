N, M = map(int, input().split())
card = list(map(int, (input().split())))
result = 0

for i in range(len(card)-2):
  for j in range(i+1, len(card)-1):
    for k in range(j+1, len(card)):
      temp = card[i] + card[j] + card[k]
      if result < temp and temp <= M:
        result = temp

print(result)

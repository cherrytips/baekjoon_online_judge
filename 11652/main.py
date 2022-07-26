N = int(input())
cards = {}
max = 0

for i in range(N):
  card = int(input())

  if card not in cards:
    cards[card] = 1
  else:
    cards[card] += 1

keys = list(cards.keys())
keys.sort()
result = keys[len(keys)-1]

for c in keys:
  if max < cards.get(c) and c < result:
    result = c

print(result)

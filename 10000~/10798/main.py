words = []
max = 0
answer = ''

for i in range(5):
  words.append(list(input()))

for w in words:
  if len(w) > max:
    max = len(w)

for i in range(max):
  for j in range(5):
    if len(words[j]) <= i:
      continue
    else:
      answer += words[j][i]

print(answer)

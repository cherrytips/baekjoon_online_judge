N = int(input())
words = []
for i in range(N):
  words.append(input())
result = 0

for word in words:
  temp = []
  for i in range(len(word)):
    if word[i] not in temp:
      temp.append(word[i])
    elif word[i-1] == word[i]:
      continue
    else:
      result -= 1
      break
  result += 1

print(result)

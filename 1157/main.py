word = input().upper()
result = {}
cnt = []

for w in word:
  if w not in result:
    result[w] = 1
  else:
    result[w] += 1

cnt = list(result.values())
cnt.sort(reverse=True)

if len(cnt) == 1:
  for r in result:
    print(r)
    break
elif cnt[0] == cnt[1]:
  print('?')
else:
  for r in result:
    if result[r] == cnt[0]:
      print(r)
      break

N = int(input())
arr = []

for i in range(50):
  arr.append([])

for i in range(N):
  word = input()
  if word in arr[len(word)-1]:
    continue
  else:
    arr[len(word)-1].append(word)

for a in arr:
  if len(a) == 0:
    continue
  a.sort()
  for ai in a:
    print(ai)

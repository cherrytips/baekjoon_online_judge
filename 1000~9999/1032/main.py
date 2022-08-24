N = int(input())
searches = []

for i in range(N):
  searches.append(input())

result = list(searches[0])

for file in searches:
  for i in range(len(file)):
    if result[i] != file[i]:
      result[i] = '?'

result = ''.join(result)
print(result)

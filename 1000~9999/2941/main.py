word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = 0
cnt = 0

for c in croatian:
  if c in word:
    result += word.count(c)
    cnt += word.count(c)
    word = word.replace(c, '/')

result += (len(word)-cnt)
print(result)

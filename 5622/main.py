word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in word:
  for j in dial:
    if i in j:
      result += (dial.index(j)+3)
      break

print(result)

S = input()
remain = ''

for s in S:
  remain += s

  if remain[-2:] == '()':
    remain = remain[:-2]

print(len(remain))

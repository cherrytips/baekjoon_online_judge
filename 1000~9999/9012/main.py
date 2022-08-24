T = int(input())

for t in range(T):
  ps = input()
  vps = ''

  for p in ps:
    vps += p
    if vps[-2:] == '()':
      vps = vps[:-2]

  if len(vps) == 0:
    print('YES')
  else:
    print('NO')

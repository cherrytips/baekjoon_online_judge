S = list(input())

for s in range(len(S)):
  rot = ord(S[s])+13

  if ord('A') <= ord(S[s]) and ord(S[s]) <= ord('Z'):
    if rot <= 90:
      S[s] = chr(rot)
    else:
      S[s] = chr(rot-26)
  elif ord('a') <= ord(S[s]) and ord(S[s]) <= ord('z'):
    if rot <= 122:
      S[s] = chr(rot)
    else:
      S[s] = chr(rot-26)

print(''.join(S))

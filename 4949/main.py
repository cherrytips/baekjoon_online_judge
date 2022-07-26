while True:
  sentence = input()
  balance = ''

  if sentence == '.':
    break
  else:
    for s in sentence:
      if s == '(' or s == ')' or s == '[' or s == ']':
        balance += s
        if balance[-2:] == '()' or balance[-2:] == '[]':
          balance = balance[:-2]

  if balance == '':
    print('yes')
  else:
    print('no')

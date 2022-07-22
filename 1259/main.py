while True:
  num = input()
  length = len(num)
  result = 'yes'

  if int(num) == 0:
    break

  for i in range(int(length/2)):
    if num[i] != num[len(num)-i-1]:
      result = 'no'
      break

  print(result)

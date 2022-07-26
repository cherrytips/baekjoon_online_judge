T = int(input())
numbers = [int(input()) for _ in range(T)]

for num in numbers:
  answer = 0
  temp = 1

  for n in range(1, num+1):
    temp *= n
    ch = str(temp)
    index = -1

    if ch[index] == '0':
      while ch[index-1] == '0':
        index -= 1

      ch = ch[index-1:index]
      answer -= index
      temp = int(ch)

  print(answer)

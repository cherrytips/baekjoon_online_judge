T = int(input())
answer = []

for i in range(T):
  sentence = input().split()

  for s in range(len(sentence)):
    sentence[s] = ''.join(list(reversed(sentence[s])))

  sentence = ' '.join(sentence)
  print(sentence)

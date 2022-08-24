N, M = map(int, input().split())
dic_num = {}
dic_name = {}

for i in range(N):
  pok = input()
  dic_num[i+1] = pok
  dic_name[pok] = i+1

for i in range(M):
  quest = input()

  if quest.isnumeric():
    print(dic_num.get(int(quest)))
  else:
    print(dic_name.get(quest))

'''
1 4 10 20 35
1 3 6 10 15
1 2 3 4 5
'''
T = int(input())


def get_sum_list(list):
  temp = []
  for i in range(len(list)):
    num = 0
    for j in range(i+1):
      num += list[j]
    temp.append(num)
  return temp


for i in range(T):
  k = int(input())
  n = int(input())
  result = 0
  person = []

  for j in range(n):
    person.append(j+1)

  for j in range(k):
    person = get_sum_list(person)

  print(person[len(person)-1])

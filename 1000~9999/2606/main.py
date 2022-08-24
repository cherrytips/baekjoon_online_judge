com = int(input())
net = int(input())
infect = set()

nets = []
for i in range(net):
  temp = list(map(int, input().split()))
  nets.append(temp)
  nets.append(list(reversed(temp)))
nets.sort()

print(nets)

for n in nets:
  s1, s2 = n[0], n[1]

  if s1 == 1:
    infect.add(s2)
  elif s1 in infect:
    infect.add(s2)

print(infect)
print(len(infect)-1)

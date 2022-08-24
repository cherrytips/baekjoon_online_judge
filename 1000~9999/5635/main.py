n = int(input())
students = []

for i in range(n):
  students.append(list(input().split()))

min = students[0]
max = students[0]

for s in students:
  if int(min[3]) < int(s[3]):
    min = s
  elif int(min[3]) == int(s[3]) and int(min[2]) < int(s[2]):
    min = s
  elif int(min[3]) == int(s[3]) and int(min[2]) == int(s[2]) and int(min[1]) < int(s[1]):
    min = s

  if int(max[3]) > int(s[3]):
    max = s
  elif int(max[3]) == int(s[3]) and int(max[2]) > int(s[2]):
    max = s
  elif int(max[3]) == int(s[3]) and int(max[2]) == int(s[2]) and int(max[1]) > int(s[1]):
    max = s

print(min[0])
print(max[0])

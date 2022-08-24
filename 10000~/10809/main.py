S = list(input())

result = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for s in S:
    if s in result:
        result[result.index(s)] = S.index(s)

for i in range(len(result)):
    if type(result[i]) == str:
        result[i] = -1
    if i == len(result)-1:
        break
    print(result[i], end=' ')
print(result[len(result)-1])

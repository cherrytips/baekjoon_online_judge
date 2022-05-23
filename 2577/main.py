A = int(input())
B = int(input())
C = int(input())
calculated = list(str(A*B*C))

count = []
for i in range(10):
    count.append(0)

for i in calculated:
    count[int(i)] += 1

for i in count:
    print(i)

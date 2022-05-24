rest = set()

for i in range(10):
    num = int(input())
    rest.add(num % 42)

print(len(rest))

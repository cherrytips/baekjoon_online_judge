A, B = map(int, input().split())
arr = []
num = 1
count = 0
result = 0

for i in range(B):
  if num == count:
    num += 1
    count = 0
  arr.append(num)
  count += 1

  if i >= A-1:
    result += num

print(result)

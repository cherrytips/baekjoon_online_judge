A, B = map(list, input().split())
result = []
cnt = 0

A.reverse()
B.reverse()

if len(A) >= len(B):
  while cnt < len(B):
    result.append(int(A[cnt])+int(B[cnt]))
    cnt += 1
  if len(A) != len(B):
    while cnt < len(A):
      result.append(int(A[cnt]))
      cnt += 1
elif len(A) < len(B):
  while cnt < len(A):
    result.append(int(A[cnt])+int(B[cnt]))
    cnt += 1
  while cnt < len(B):
    result.append(int(B[cnt]))
    cnt += 1

for i in range(len(result)):
  if result[i] >= 10:
    temp = result[i]//10
    result[i] %= 10
    if i+1 == len(result):
      result.append(temp)
    else:
      result[i+1] += temp

result.reverse()

answer = ''
for i in result:
  answer += str(i)
print(answer)

N = int(input())
files = [input().split('.')[1] for _ in range(N)]
answer = []
cnt = 1

files.sort()

for i in range(N):
  if i == N-1:
    temp = files[i]+' '+str(cnt)
    answer.append(temp)
  elif files[i] != files[i+1]:
    temp = files[i]+' '+str(cnt)
    answer.append(temp)
    cnt = 1
  else:
    cnt += 1

for a in answer:
  print(a)

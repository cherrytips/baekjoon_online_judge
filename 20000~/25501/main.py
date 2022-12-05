import sys
read = sys.stdin.readline


def recursion(str_t, l, r, cnt):
  if l >= r:
    return 1, cnt+1
  if str_t[l] != str_t[r]:
    return 0, cnt+1
  else:
    return recursion(str_t, l+1, r-1, cnt+1)


T = int(read())

for _ in range(T):
  str_t = read().strip()
  value, cnt = recursion(str_t, 0, len(str_t)-1, 0)
  print(value, cnt)

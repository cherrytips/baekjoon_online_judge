A, B, C = map(int, input().split())
break_even_point = 1

if B >= C:
  break_even_point = -1
else:
  break_even_point = int(A/(C-B)) + 1

print(break_even_point)

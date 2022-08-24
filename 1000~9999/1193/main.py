'''
1 2 4 7 11 16
3 5 8 12 17
6 9 13 18
10 14 19
15 20
21
'''
X = int(input())
line = 0
end = 0

while X > end:
  line += 1
  end += line

diff = end-X
if line % 2 == 0:
  top = line-diff
  bottom = 1+diff
else:
  top = 1+diff
  bottom = line-diff

print(f'{top}/{bottom}')

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
count = 0

for i in range(x-1):
  count += days[i]
count = (count+y) % 7

if count == 0:
  print('SUN')
if count == 1:
  print('MON')
if count == 2:
  print('TUE')
if count == 3:
  print('WED')
if count == 4:
  print('THU')
if count == 5:
  print('FRI')
if count == 6:
  print('SAT')

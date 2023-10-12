import sys
readline = sys.stdin.readline

max_ = 0
row_ = 1
col_ = 1

for row in range(1, 10):
    numbers = list(map(int, readline().split()))
    if max(numbers) > max_:
        max_ = max(numbers)
        row_ = row
        col_ = numbers.index(max_)+1

print(max_)
print(row_, col_)

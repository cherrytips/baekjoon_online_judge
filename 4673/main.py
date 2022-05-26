def self_number(n):
    res = n
    n = list(str(n))
    for num in n:
        res += int(num)
    return res


not_self = []

for i in range(1, 10001):
    if i not in not_self:
        print(i)
    not_self.append(self_number(i))

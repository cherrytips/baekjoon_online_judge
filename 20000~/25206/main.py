import sys
readline = sys.stdin.readline

rank_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
            'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

grade_sum = 0
total_sum = 0

for _ in range(20):
    subject, grade, rank = readline().split()

    if rank == 'P':
        continue

    grade_sum += float(grade)
    total_sum += (float(grade)*rank_dic[rank])

print(round(total_sum/grade_sum, 6))

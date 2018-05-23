#https://www.hackerrank.com/challenges/nested-list/problem
grades = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    grades.append((name, score))

grades_sorted = sorted(grades, key=lambda grade: (grade[1], grade[0]))
# for i, j in enumerate(grades_sorted):
#     print '{} {}: {} '.format(i+1, j[0], j[1])

second_lowest = sorted(list(set([grade for name, grade in grades_sorted])))[1]

for student in grades_sorted:
    if student[1] == second_lowest:
        print student[0]

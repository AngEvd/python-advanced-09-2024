students_number = int(input())

students = {}

for _ in range(students_number):
    student, grade = input().split()

    if student not in students:
        students[student] = []

    students[student].append(float(grade))

for student, grades in students.items():
    print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {sum(grades) / len(grades):.2f})")

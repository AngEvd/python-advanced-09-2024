def softuni_students(*args, **kwargs):
    result = ""
    students = {}
    invalid_course = []
    for arg in args:
        try:
            students[arg[1]] = kwargs[arg[0]]
        except KeyError:
            invalid_course.append(arg[1])

    sorted_students = dict(sorted(students.items(), key=lambda kvp: kvp[0]))
    invalid_course.sort()
    for student, course in sorted_students.items():
        result += f"*** A student with the username {student} has successfully finished the course {course}!\n"
    if invalid_course:
        result += f"!!! Invalid course students: " + ", ".join(invalid_course)

    return result


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))



def students_credits(*args) -> str:
    DIPLOMA_CREDITS = 240
    dyan_credits = 0
    dyan_courses = {}
    for course in args:
        course_name, credit, max_points, points = course.split("-")
        course_credits = int(credit) * (int(points) / int(max_points))
        dyan_courses[course_name] = course_credits
        dyan_credits += course_credits

    if dyan_credits >= DIPLOMA_CREDITS:
        result = f"Diyan gets a diploma with {dyan_credits:.1f} credits.\n"
    else:
        result = f"Diyan needs {DIPLOMA_CREDITS - dyan_credits:.1f} credits more for a diploma.\n"

    for course, credit in sorted(dyan_courses.items(), key=lambda kvp: -kvp[1]):
        result += f"{course} - {credit:.1f}\n"

    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


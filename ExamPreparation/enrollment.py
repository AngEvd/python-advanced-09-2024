def gather_credits(credits_goal: int, *args: tuple) -> str:
    credits_gathered = 0
    enrollments = []
    for course_name, course_credits in args:
        if credits_gathered >= credits_goal:
            break
        if course_name in enrollments:
            continue
        enrollments.append(course_name)
        credits_gathered += course_credits

    if credits_gathered >= credits_goal:
        return f"Enrollment finished! Maximum credits: {credits_gathered}.\nCourses: {', '.join(sorted(enrollments))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_goal - credits_gathered} credits more."



print(gather_credits(
            80,
            ("Basics", 27),

        ))
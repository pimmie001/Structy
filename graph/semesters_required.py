def semesters_required(num_courses, prereqs):
    my_dict = {}
    for i in range(num_courses):
        my_dict[i] = []
    for a,b in prereqs:
        my_dict[b].append(a)

    courses = set(range(num_courses))
    count = 0
    while courses:
        count += 1
        courses = get_prereqs(courses, my_dict)
    return count


def get_prereqs(courses, my_dict):
    # returns the required courses that need to be followed before following all these courses

    result = set()
    for course in courses:
        for prereq in my_dict[course]:
            result.add(prereq)
    return result


def test_case():
    return [
        "3 2",
        "0123 9876 2222",
        "2 1 8888 2222",
        "3 2 9876 2222 7654",
        "3 2",
        "0123 9876 2222",
        "2 2 8888 2222",
        "3 2 7654 9876 2222",
        "0"
    ]
lines = test_case()

def a (line):
    return _a(line, [])

def _a(line, degrees):
    if line == "0":
        return degrees

    tmp = line.split(" ")
    ncategories = int(tmp[1])
    ncourses = int(tmp[0])
    courses = input().split(" ")
    degree = True
    for i in range(ncategories):
        category = input().split(" ")
        category_courses = int(category.pop(0))
        min_courses = int(category.pop(0))
        courses_valid = [ x for x in category if x in courses]
        if len(courses_valid) < min_courses:
            degree = False

    if degree:
        degrees.append("yes")
    else:
        degrees.append("no")
    line = input()
    return _a(line, degrees)

def run():
    result = a(input())
    for r in result:
        print(r)

run()

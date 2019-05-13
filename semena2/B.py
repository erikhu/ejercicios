def test_case():
    return [
        "1",
        "7",
        "a 3",
        "W 10",
        "A 100",
        ", 10",
        "k 7",
        ". 3",
        "I 13",
        "7",
        """ACM International Collegiate Programming Contest (abbreviated
as ACM-ICPC or just ICPC) is an annual multi-tiered competition
among the universities of the world. The ICPC challenges students
to set ever higher standards of excellence for themselves
through competition that rewards team work, problem analysis,
and rapid software development.
From Wikipedia."""
    ]

is_testing = False
lines = test_case()

def custom_input():
    if is_testing:
        return lambda : lines.pop(0)
    else:
        return input

def b(custom_input):
    n = int(custom_input())
    for n in range(n):
        k = int(custom_input())
        characters = {}
        for i in range(k):
            tmp = str.split(custom_input())
            characters[tmp[0]] = float(tmp[1])/100
        m = custom_input()
        article = custom_input().split("\n")
        total = 0.0
        for i in range(int(m)):
            for key in characters.keys():
                total = total + article[i].count(key) * characters[key]
        print("%s$" % round(total, 2))

def run():
    b(custom_input())

run()

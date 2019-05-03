H = 0 #height hole
U = 1 #distance snail can climb
D = 2 #distance slide down
F = 3 #fatige factor in percent

def d(case):
    days = 1
    climb_distance = int(case[U])
    climbed = climb_distance
    fatige = climb_distance * int(case[F])/100
    print(case)
    while(climbed > 0 and climbed < int(case[H])):
        climbed = climbed - int(case[D])
        if(climbed < 0):
            break
        days = days + 1
        climb_distance = climb_distance - fatige
        climbed = climbed + climb_distance

    if climbed > int(case[H]):
        print("success on day %s" % days)
    else:
        print("failure on day %s" % days)

def test_case():
    return ["6 3 1 10",
    "10 2 1 50",
     "50 5 3 14",
     "50 6 4 1",
     "50 6 3 1",
     "1 1 1 1",
     "0 0 0 0"]

def run():
    for case in test_case():
        if (str.split(case)[H] != "0"):
            d(str.split(case," "))

run()

k =  int(input())
donation = 0
for i in range(k):
    operation = str.split(input())
    if operation[0] == "donate":
        donation += int(operation[1])
    elif operation[0] == "report":
        print(donation)

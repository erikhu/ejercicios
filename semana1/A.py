value = input()
while(value != "End of File"):
    numbers = str.split(value, " " )
    print(int(numbers[1]) - int(numbers[0]))
    value = input()

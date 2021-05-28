
while True:
    try:
        x = int(input("Enter an integer number : "))
        print(x)
        break
    except ValueError:
        print("That was not valid number. Try again...")

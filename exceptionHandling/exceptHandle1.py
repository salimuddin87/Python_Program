
while True:
    try:
        x = int(raw_input("Enter an integer number : "))
        print x
        break
    except ValueError:
        print "That was not valid number. Try again..."

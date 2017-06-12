while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except KeyboardInterrupt:
        print("KeyboardInterrupt!!")
    except ValueError:
        print("Oops!  That was no valid number.  Try again")


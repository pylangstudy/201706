while True:
    try:
        x = int(input("Please enter a number: "))
        print("try文完了！")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again")


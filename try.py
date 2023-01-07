while True:
    try:
        x = int(input("PLease enter a number: "))
        break
    except ValueError:
        print("opps, that was no valid number")

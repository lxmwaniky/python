while True:
    try:
        x = int(input("Enter a value for X: "))
    except ValueError:
        print("x should be an integer")
    else:
        break
print(f"x is {x}")
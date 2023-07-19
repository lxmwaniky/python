try:
    x = int(input("Enter a value for X: "))
    print(f"x is {x}")
except ValueError:
    print("x should be an integer")
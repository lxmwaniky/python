try:
    x = int(input("Enter a value for X: "))
    print(x)
except ValueError:
    print("x should be an integer")
def main():
     x = get_int()
     print(f"x is {x}")

def get_int():
    while True:
            try:
                x = int(input("Enter a value for X: "))
            except ValueError:
                print("x should be an integer")
            else:
                break
    return x

main()
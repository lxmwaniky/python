def main():
     x = get_int()
     print(f"x is {x}")

def get_int():
    while True:
            try:
                return int(input("Enter a value for X: "))
            except ValueError:
                pass
            
main()
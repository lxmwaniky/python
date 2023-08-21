def main():
    while True:
        try:
            x = int(input("Enter a number: "))
            y = x%2
            print(y)
        except ValueError:
            print("Enter an Integer")
            break

main()

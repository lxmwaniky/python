user = "Alex Mwaniki"
pin = 1234
attempts = 2
while True:
    try:
        epin = int(input("Enter your PIN: "))
        if epin != pin and attempts > 0:
            attempts -= 1
            print(f"Invalid PIN. {attempts+1} attempts left")
        elif attempts <= 1:
            print("LINE BLOCKED!!!")
            break
        else:
            print(f"Welcome, {user}")
            break
    except ValueError:
        print("PIN must be an integer")

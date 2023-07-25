def decimal_to_binary(number):
    binary = ""
    if number == 0:
        return "0"
    
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2
    
    return binary

# Prompting the user for input
while True:
    try:
        number_to_convert = int(input("Decimal: "))
        binary_result = decimal_to_binary(number_to_convert)
        print(f"Binary: {binary_result}")
        break
    except ValueError:
        None

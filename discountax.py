def calculate_total_cost(num_kaleidoscopes):
    kaleidoscope_cost = 5.00
    discount_rate = 0.10
    tax_rate = 0.07

    if num_kaleidoscopes > 1:
        total_cost = num_kaleidoscopes * kaleidoscope_cost * (1 - discount_rate)
    else:
        total_cost = num_kaleidoscopes * kaleidoscope_cost

    total_cost_with_tax = total_cost * (1 + tax_rate)
    return round(total_cost_with_tax, 2)

num_kaleidoscopes = int(input("Enter the number of kaleidoscopes you want to buy: "))

total_cost = calculate_total_cost(num_kaleidoscopes)

print(f"The total price is: ${total_cost:.2f}")

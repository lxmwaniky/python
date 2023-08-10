def main():
    grocery_list = {}
    try:
        while True:
            item = input().lower()
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    sorted_list = sorted(grocery_list.items(), key=lambda x: x[0])

    print("\nYour Grocery List:")
    for item, count in sorted_list:
        print(f"{count} {item.upper()}")

main()
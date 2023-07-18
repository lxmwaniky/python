def main():
    camel = input("camelCase: ")
    converted = camel2snake(camel)
    print(f"snake_case: {converted}")

def camel2snake(n):
    snake = ""
    for char in n:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake.lstrip("_")


main()
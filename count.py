def count_letters(word):
    return len(word)

def main():
    user_input = input("Enter a word: ")
    letter_count = count_letters(user_input)
    print(f"The word '{user_input}' has {letter_count} letters.")

if __name__ == "__main__":
    main()

def check_condition(sentence):
    words = sentence.split()
    prev_last_letter = None

    for word in words:
        first_letter = word[0].lower()
        if prev_last_letter is not None and prev_last_letter != first_letter:
            return False
        prev_last_letter = word[-1].lower()

    return True

input_sentence = input("Enter a sentence: ")

result = check_condition(input_sentence)
print(result)

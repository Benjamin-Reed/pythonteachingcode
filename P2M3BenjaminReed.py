

# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  

def word_mixer(original_list):
    original_list.sort()

    new_words = []

    while len(original_list) > 5:
        new_words.append(original_list.pop(-5))

        new_words.append(original_list.pop(0))

        new_words.append(original_list.pop(-1))

    return new_words

poem_input = input("Welcome Ben Reed, enter a saying or peom: ")

word_list = poem_input.split()

list_length = len(word_list)

for word_string in range(list_length):
    word = word_list[word_string]
    word_length = len(word)

    if word_length <= 3:
        word_list[word_string] = word.lower()

    elif word_length >= 7:
        word_list[word_string] = word.upper()


mixed_words_list = word_mixer(word_list)

print(" ".join(mixed_words_list))



def permutations(input_str, current_per=""):
    if not input_str:
        print(current_per)
        return

    for i in range(len(input_str)):
        current_char = input_str[i]

        remaining_chars = input_str[:i] + input_str[i + 1:]

        permutations(remaining_chars, current_per + current_char)


n = input("Input: ")
permutations(n)

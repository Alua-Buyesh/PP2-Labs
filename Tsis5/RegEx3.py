import re

def find_sequences(text):
    pattern = r'[a-z_]+[a-z]'
    matches = re.findall(pattern, text)
    return matches

text = "This_is a test_with_some_sequences_of_lowercase_letters_joined_with_underscore."
matches = find_sequences(text)
print(matches)


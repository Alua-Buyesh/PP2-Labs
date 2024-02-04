def reverse_words(s):
    words = s.split()
    rev_w = words[::-1]
    rev = ' '.join(rev_w)

    return rev

s = input("Input: ")
res = reverse_words(s)
print("Output:", res)

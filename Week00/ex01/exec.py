import sys

args = sys.argv[1:][::-1]

def reverse_f(text):
    tex = ""
    for i in range(1, len(text) + 1):
        tex += text[len(text) - i]
    return tex

reverse_words = []
for word in args:
    reverse_word = reverse_f(word)
    reverse_words.append(reverse_word)
res = ' '.join(reverse_words)

print(res)

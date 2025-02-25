import sys

args = sys.argv[1:][::-1]

def reverse_f(text):
    tex = ""
    for i in range(1, len(text) + 1):
        tex += text[len(text) - i]
    return tex

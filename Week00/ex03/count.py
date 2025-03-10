import sys
import string


def text_analyzer(text):
    """
    text_analyzer:
                    a function that take a single string and analyze it
                    to check the upper_case character and lower_case and spces
                    and also the punctuation marks
    """
    upper_case = 0
    lower_case = 0
    space = 0
    pun = 0
    i = 0
    while i < len(text):
        if 65 <= ord(text[i]) <= 90:
            upper_case += 1
        elif 97 <= ord(text[i]) <= 122:
            lower_case += 1
        elif ord(text[i]) == 32:
            space += 1
        else:
            for c in text:
                if c in string.punctuation:
                    pun += 1
        i += 1
    print(f"{upper_case} upper letter(s)")
    print(f"{lower_case} lower letter(s)")
    print(f"{space} space(s)")
    print(f"{pun} punctuation mark(s)")

text_analyzer(sys.argv[1])

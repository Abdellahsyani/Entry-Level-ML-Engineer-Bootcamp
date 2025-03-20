import sys

def scan_words(text, num):
    res = [word for word in text.split(" ") if len(word) >= num]
    print(f"{res}")


if len(sys.argv) != 3:
    print("ERROR")
else:
    try:
        n = int(sys.argv[2])
        scan_words(sys.argv[1], n);
    except ValueError:
        print("ERROR")

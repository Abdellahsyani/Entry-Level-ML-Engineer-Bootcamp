import sys

def checks(arg):
    try:
        if not arg.isnumeric():
                raise ValueError("the argument must be integer")
        number = int(arg)
    except ValueError as n:
        print(n)
        return
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

if len(sys.argv) > 1:
    checks(sys.argv[1])
else:
    print("no argumenet")

kata = "The right format"

leng = len(kata)

c = 1
while c < 42:
    print("-", end="")
    if (c + leng == 42):
        print(f"{kata}", end="")
        break
    c += 1

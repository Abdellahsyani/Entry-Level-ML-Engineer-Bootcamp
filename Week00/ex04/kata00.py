kata = (19,42,21)

print(f"The {len(kata)} number are: ", end="")
for i, k in enumerate(kata):
    print(f" {k}", end="")
    if (i != len(kata) - 1):
        print(",", end="")

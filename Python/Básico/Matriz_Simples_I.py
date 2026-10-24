i = 0
while i <= 8:
    print(f"linha {i}: | ", end="")
    
    j = 0
    while j <= 8:
        print(f"{i}{j}", end=" ")
        j = j + 1 # ou j += 1

    print("|")

    i = i + 1 # ou i += 1
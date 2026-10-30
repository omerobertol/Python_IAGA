s = input()

n = len(s)

for i in range(3): # faz 3 linhas
    for j in range(n): # percorre a string
        print(s[j], end= " ")

    print()
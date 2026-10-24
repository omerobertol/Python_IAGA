def fatorial(n):
    if (n < 0): # não tem fatorial de número negativo
        return 0

    f = 1
    for i in range(2, n+1):
        f = f * i

    return(f)

# módulo principal (main)
for n in range(0, 11):
    print(f"{n}! = {fatorial(n)}")
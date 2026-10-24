n = int(input("n = "))

print()

if n < 0:
    result = "negativo"

if n == 0:
    result = "neutro"

if n > 0:
    result = "positivo"

print(f"O número {n} é <<< {result} >>>")
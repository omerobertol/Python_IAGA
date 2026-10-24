n = int(input("n = "))

print()

if n < 0:
    result = "negativo"
elif n == 0:
    result = "neutro"
else:
    result = "positivo"

print(f"O número {n} é <<< {result} >>>")
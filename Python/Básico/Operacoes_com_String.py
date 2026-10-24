s = input("Informe uma String: ")

print()
print(s.upper()) # em maiúsculas
print(s.lower()) # em minúsculas
print("[" + s.center(40) + "]")
print("[" + s.center(40, '*') + "]")

s = s.replace("A", "@") # substitui A por @
s = s.replace("a", "@") # substitui a por @
s = s.replace("Á", "@") # substitui Á por @
s = s.replace("á", "@") # substitui á por @
print(s) 

print(s.split(" ")) # separa a string em uma lista de palavras
print(f"@ existe {s.count("@")} vezes na String")
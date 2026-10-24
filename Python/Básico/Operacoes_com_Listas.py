# lendo os itens da lista todos em uma mesma linha, 
# separados por espaço
a = [int(item) for item in input().split(" ")]

print()
item = int(input("Digite o item a ser buscado na lista: "))

print()
print(a)
print("Tamanho =", len(a))
print("Soma    =", sum(a))
print("Média   =", sum(a) / len(a))
print("Menor   =", min(a))
print("Maior   =", max(a))

print()
print(f"O item {item} existe {a.count(item)} vez(es) na lista.")

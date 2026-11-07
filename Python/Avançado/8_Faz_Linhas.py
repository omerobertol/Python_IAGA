def linha(tipo="-", tam=20):
    result = ""
    for i in range(tam):
        result += tipo

    return result

# módulo principal (main)
print(linha("-", 20), end="]")
print(linha("<<ABC>>", 5))
print()
print(linha())
print(linha(tipo="X"))
print(linha(tam=10))
print(linha(tipo="JUCA", tam=3))
import Vetor

a = Vetor.entrada("Vetor A", 5)
b = Vetor.entrada("Vetor B", 7) 

print(Vetor.toString("Vetor A", a))

print()
print(Vetor.saida("Vetor B", b))
print("Menor Valor =", Vetor.menor_Valor(b))
print("Maior Valor =", Vetor.maior_Valor(b))
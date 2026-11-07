import MeuMath

a = int(input("a: "))
b = int(input("b: "))

# instanciando (criando) um objeto da classe MeuMath
# inicializando o ciclo de vida do objeto "meusDados"
meusDados = MeuMath.MeuMath(a, b) # usando o modelo OO

# chamando o método __str__() do objeto "meusDados"
print()
print(meusDados) 

# no modelo modular chamamos assim:
# print(meusDados.toString())

# no modelo orientado a objetos chamamos assim:
# chama o método __str__() do objeto "meusDados"
# print(meusDados.__str__())
# print(meusDados)
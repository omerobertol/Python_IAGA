from Data import Data

a = Data(dataDeHoje=False, dia=15, mes=8, ano=1990)
aa = Data(dataDeHoje=False, dia=15, mes=12, ano=1990)
b = Data() # data de hoje
c = Data(dataDeHoje=False, dia=1, mes=1, ano=2000)

# 'a' é uma data de nascimento, então vamos mostrar a idade
print(a.toString(mostrarIdade=True))
print(aa.toString(mostrarIdade=True))

print("Hoje é dia", b.toString())
print(c.toString())
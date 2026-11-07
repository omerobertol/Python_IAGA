# random é uma biblioteca padrão do python
# isto significa que random já vem instalado com o python
from random import randint

def descricao_unidade(i):
    unidades = ('zero', 'um', 'dois', 'tres', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove')

    return(unidades[i])

# Módulo principal (main)
n = int(input("Quantas unidades serão sorteadas? "))

print()
for i in range(n):
    unid = randint(0, 9)

    print(f"{unid}: {descricao_unidade(unid)}")
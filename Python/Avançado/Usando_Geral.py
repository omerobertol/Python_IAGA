from random import randint
import Geral

Geral.cls()

for i in range(10):
    nro = randint(1, 100)
    print(f"{i+1}o. numero: {nro}")

    Geral.delay(1) # delay de 1 segundo
    print(Geral.linha())


print("Fim do programa!")
Geral.parada()

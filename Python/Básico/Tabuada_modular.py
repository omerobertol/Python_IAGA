# aplicando a ideia de modularização, 
# vamos criar um módulo chamado "tabuada" 
# que contém a função "tabuada(n)" que 
# imprime a tabuada do número "n". 
# Em seguida, no módulo principal, chamaremos 
# essa função para imprimir as tabuadas de 5, 7 e 9.

# módulo "tabuada"
# "n" é o parâmetro da função "tabuada"
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()

# módulo principal (main)
tabuada(5) # 5 é um parâmetro (ou argumento) passado para a função "tabuada"
tabuada(7)
tabuada(9)
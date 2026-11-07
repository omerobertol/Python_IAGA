n = int(input("n: "))

print()

# 1. abre o arquivo de texto (mode de abertura 'w' - write)
arq = open("tabuada.txt", "w")

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

    # 2. grava a linha no arquivo de texto
    arq.write(f"{n} x {i} = {n*i}\n")

# 3. fecha o arquivo de texto
arq.close()
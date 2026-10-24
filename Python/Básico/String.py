while True:
    s = input("Digite uma string (ou 'FIM' para encerrar):\n")
    if s.upper() == "FIM":
        break

    print()

    # faz uma matriz de caracteres, 
    # com cada linha contendo os caracteres da string 
    # até a posição i
    for i in range(len(s)): # linhas
        for j in range(i+1): # colunas
            print(s[j], end="|")
        print()

    print()


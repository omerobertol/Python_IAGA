from Geral import cls, parada

cls()
while True:
    nomeArquivo = input("Informe o nome do arquivo (FIM para encerrar):\n")
    if nomeArquivo.upper() == "FIM":
        break

    print()

# mecanismo de tratamento de exceção (try/except)
    try:
        # trecho de código-fonte PROTEGIDO
        arquivo = open(nomeArquivo, "r")
        # lê "todas" as linhas do arquivo de texto
        linhas = arquivo.readlines()
        print("*** Conteúdo do arquivo:")
        for linha in linhas:
            print(linha, end="")

        print()
        parada()
        arquivo.close()
        cls()
    except FileNotFoundError:
        print(f"Erro: o arquivo \"{nomeArquivo}\", não foi encontrado.\n")

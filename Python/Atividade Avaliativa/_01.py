# Faça um programa para ler um valor monetário (R$) 
# de um produto e calcule um desconto fixo de 10%. 
# Calcule também o valor final do produto. 
# Apresente os valores como apresentado na 
# coluna “Resultados”.

# entrada de dados
vlrProduto = float(input())

# processamento
desconto = vlrProduto * (10 / 100)
vlrFinal = vlrProduto - desconto

# saída de dados
print(f"Valor do Produto  = R$ {vlrProduto:.2f}")
print(f"Valor do Desconto = R$ {desconto:.2f}")
print(f"Valor Final       = R$ {vlrFinal:.2f}")
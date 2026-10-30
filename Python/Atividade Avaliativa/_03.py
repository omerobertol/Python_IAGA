vlrProduto = float(input())

if vlrProduto < 5000.00:
    desconto = vlrProduto * (10 / 100)
    desc = 10
else:
    desconto = vlrProduto * (15 / 100)
    desc = 15

vlrFinal = vlrProduto - desconto

print(f"Valor do Produto        = R$ {vlrProduto:.2f}")
print(f"Valor do Desconto ({desc}%) = R$ {desconto:.2f}")
print(f"Valor Final             = R$ {vlrFinal:.2f}")
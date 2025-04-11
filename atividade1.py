# 1.A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias de queijo,
# uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo ou presunto pesa 50 gramas,
# e que a rodela de hambúrguer pesa 100 gramas,faça um algoritmo em que o dono forneça a quantidade de sanduíches a fazer,
# e a máquina informe as quantidades (em quilos) de queijo, presunto e carne necessários para compra.

lanche = int(input("Insira a Quantidade de lanches que deseja Fazer:"))

presunto = lanche * 0.050
queijo = lanche * 0.0100
hamburguer = lanche * 0.0100

print("A quantidade a se-comprar de presunto é :",presunto,"kg")
print("A quantidade a se-comprar de queijo é :",queijo,"kg")
print("A quantidade a se-comprar de hamburguer é :",hamburguer,"kg")
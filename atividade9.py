#  Um tonel de refresco é feito com 8 partes de água mineral e 2 partes de suco de maracujá.
#  Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).

#Inserção 
tonel = float(input("Digita a quantidaded desejada de litros de refresco (Em Litros) : "))

#Calculo de Proporção
agua = (tonel * 0.8)
suco = (tonel * 0.2)

#imprimi
print("A Quantidade de suco Litros : ",suco," L")# 8 partes de 10 partes e 80% (8 partes de suco e 2 de agua)
print("A Quantidade de agua Litros : ",agua," L")# 2 partes de 10 partes e 20% (8 partes de suco e 2 de agua)



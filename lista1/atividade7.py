#  Pedrinho tem um cofrinho com muitas moedas,
#  e deseja saber quantos reais conseguiu poupar.
#  Faça um algoritmo para ler a quantidade de cada tipo de moeda,
#  e imprimir o valor total economizado, em reais.
#  Considere que existam moedas de 1, 5, 10, 25 e 50 centavos,
#  e ainda moedas de 1 real.
#  Não havendo moeda de um tipo,
#  a quantidade respectiva é zero.

#Inserção 
print ("(Digite 0 Caso não tenha nem uma moeda)")
moeda1 = float(input ("Digite quantas moedas tem R$ de 0,01 : "))
moeda2 = float(input ("Digite quantas moedas tem R$ de 0,05 : "))
moeda3 = float(input ("Digite quantas moedas tem R$ de 0,10 : "))
moeda4 = float(input ("Digite quantas moedas tem R$ de 0,25 : "))
moeda5 = float(input ("Digite quantas moedas tem R$ de 0,50 : "))
moeda6 = float(input ("Digite quantas moedas tem R$ de 1    : "))

#Calculo
total1 = moeda1 * 0.01
total2 = moeda2 * 0.05
total3 = moeda3 * 0.10
total4 = moeda4 * 0.25
total5 = moeda5 * 0.50
total6 = moeda6 * 1

#Soma 
valor_total = ( total1 + total2 + total3 + total4 + total5 + total6 )

#imprimi
print (f"O valor total de todas moedas é R$ {valor_total:.2f}") # Colocar :.2f pois senão fica aparecendo muitas casas decimais ex: 1.0000000000000001

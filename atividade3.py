#3.A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.
#Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um determinado funcionário.
#Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

horario = float(input("Insira a quantiddade de horas trabalhadas: "))

salario_normal = horario * 10

hora_extra = 0

if horario > 8:
   hora_extra =  (horario - 8) * 15
salario_bruto = salario_normal + hora_extra

print("O salario Bruto é :",salario_bruto)  
print("O salario liquido é :",salario_bruto - (salario_bruto * 0.1))
 
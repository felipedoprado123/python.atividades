#  Faça um algoritmo que receba dois números,
#  calcule e mostre a divisão do primeiro número pelo segundo.
#  Sabe-se que o segundo número não pode ser zero,
#  portanto não é necessário se preocupar com validações.

#desclarar a variavel
contador = 1

#repeticao caso coloque 0
while contador == 1:
    num1 = float(input("Insira o Primeiro número : "))
    num2 = float(input("Insira o Segundo número : "))


    #Calculo
    if num2 == 0: # a condicao
     print("Digiti novamete o Segundo Numero não Aceito Numero 0")
     contador = 0 

    else:
      contador = 1
      num3 = num1 / num2 
      contador = 0

    #imprimi
    print("O Resultado Da Divisição : ",num3)
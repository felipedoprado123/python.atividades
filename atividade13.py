#  Faça um algoritmo que receba duas notas,
#  calcule e mostre a média ponderada dessas notas,
#  considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

#Inserção
nota1 = float(input("Digite a primera nota:"))
nota2 = float(input("Digite a segunda nota:"))

#media poderada
resultado = ((nota1 * 2) + (nota2 * 3)) / 5 

#imprimi
print("A Media é : ",resultado)


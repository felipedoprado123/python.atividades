#Calcule o volume de uma caixa d'água cilíndrica.

#Inserção 
raio = float(input("Informe o raio a base do cilidro (Em METROS): "))
altura = float(input(" Informe a altura do cilidro (Em METROS): "))

#calculo do volume
volume = (raio * raio) * 3.14 * altura

#imprimi
print (f"o Volume é : {volume:.2f} M³")
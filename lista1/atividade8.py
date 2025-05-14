#  Num dia de sol, você deseja medir a altura de um prédio,
#  porém, a trena não é suficientemente longa.
#  Assumindo que seja possível medir sua sombra e a do prédio no chão,
#  e que você lembre da sua altura,
#  faça um algoritmo para ler os dados necessários e calcular a altura do prédio.

#Inserção 
sombra_pessoa = float(input("Digite a altura de sua sombra em cm : "))
altura_pessoa = float(input("Digite a sua altura em cm : "))
sombra_predio = float(input("Digite a altura da sombra do predio em cm : "))

#Calculo de Proporção
altura_predio = ( altura_pessoa  * sombra_predio) / sombra_pessoa
altura_predio = altura_predio / 100

#imprimi
print(f"A Altura do predio em metros : {altura_predio::.2f} ")


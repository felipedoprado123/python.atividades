#  A granja Frangotech possui um controle automatizado de cada frango da sua produção.
#  No pé direito do frango há um anel com um chip de identificação;
#  no pé esquerdo são dois anéis para indicar o tipo de alimento que ele deve consumir.
#  Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50,
#  faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.

# Insere a quantidade de galinhas
galinha = float(input("insira a quantidade de Galinhas na granja: "))

# calculos 
pe_direito = galinha * 4
pe_esquerdo = galinha * 7 # Número 7 pois e multiplicacao de 3,50 por 2 (Pois são 2 aneis)
valor = pe_direito + pe_esquerdo

# Resultado
print("o valor é : ",valor)
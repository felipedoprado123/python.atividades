# Variável que controla o loop principal
num = 0
contador1 = 0
contador2 = 0

# Nome autorizado
nome_autorizado = "fulano"  # você pode mudar para o nome que quiser
senha = 1234

while contador1 == 0:
    # Exibe a mensagem de boas-vindas

    print("|----------------------------------|")
    print("|-----------Seja Bem-vindo---------|")
    print("|----------------------------------|")

    nome = input("Digite seu nome: ")
    print("")

while contador2 == 0:
        if nome == nome_autorizado:
         num = input("insira a senha:")
         contador2 = 1

        elif senha == num:

         print("Acesso liberado")
         r = input("clique enter")
         contador2 = 1

        else:
         print("Acesso bloqueado")
         r = input("")
         contador1 = 0
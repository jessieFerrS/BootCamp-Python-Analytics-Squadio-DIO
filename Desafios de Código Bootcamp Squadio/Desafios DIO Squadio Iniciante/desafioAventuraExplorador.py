# Desafio: A Aventura do Explorador
#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

# Entrada
quantidade_passos = int(input())
if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")
while quantidade_passos >= 0:
    if quantidade_passos >= 0:
        for i in range(1, quantidade_passos + 1):
            if i == 1:
                print(f"Explorador: {i} passo")
            else:
                print(f"Explorador: {i} passos")
        break

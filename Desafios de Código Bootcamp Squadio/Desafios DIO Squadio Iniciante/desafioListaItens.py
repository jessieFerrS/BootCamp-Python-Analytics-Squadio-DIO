# Lista para armazenar os itens
itens = []

#TODO: Solicite os itens ao usuário

item_1 = input()
item_2 = input()
item_3 = input()

itens.append(item_1)
itens.append(item_2)
itens.append(item_3)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")

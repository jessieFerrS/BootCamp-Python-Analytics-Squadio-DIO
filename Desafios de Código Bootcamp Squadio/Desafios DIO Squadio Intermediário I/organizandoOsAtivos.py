ativos = []

#Entrada da quantidade de ativos
quantidadeAtivos = int(input())

#Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos = sorted(ativos)
for a in ativos:
    print(a)

capacidade_atual, aumento_percentual = map(int, input().split())

#TODO: Calcule a nova capacidade do disco de Mithril
def capacidade_disco(capacidade_atual, aumento_percentual):
    return int(capacidade_atual + (capacidade_atual * aumento_percentual)/100)

#TODO: Imprima a nova capacidade
print(capacidade_disco(capacidade_atual,aumento_percentual))

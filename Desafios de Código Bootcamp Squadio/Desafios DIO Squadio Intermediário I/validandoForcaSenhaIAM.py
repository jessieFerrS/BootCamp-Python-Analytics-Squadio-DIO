import re
def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = (re.findall(r'[0-9]', senha))
    tem_caractere_especial = (re.findall(r'[!@#$%^&*(),.?\":{}|<>]', senha))

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    if re.findall(r'[a-z]', senha):
        tem_letra_minuscula = True
    elif re.findall(r'[A-Z]', senha):
        tem_letra_maiuscula = True

    if tem_letra_maiuscula or tem_letra_minuscula and tem_numero and tem_caractere_especial:
        return f'Sua senha atende aos requisitos de seguranca. Parabens!'
    else:
        return f'Sua senha nao atende aos requisitos de seguranca.'


# Obtendo a senha do usuário
senha = input().strip()
# Verificando a força da senha
resultado = verificar_forca_senha(senha)
# Imprimindo o resultado
print(resultado)


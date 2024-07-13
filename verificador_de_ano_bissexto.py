def verificador_ano_bissexto():
    ano = int(input())


# Se o ano for bissexto, imprima "Bissexto".
# Caso contrário, imprima "Nao Bissexto".
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("Bissexto")
    else:
        print("Nao Bissexto")

# Fim da função verificador_ano_bissexto()
# Chamada da função para iniciar o programa
verificador_ano_bissexto()

def conta_vogais(texto):
    # Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    #  Inicialize um contador para contar as vogais:
    contador = 0
    
    
    
    # Iteramos pelos caracteres da string
    for char in texto:
        # Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
            contador += 1
        
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")
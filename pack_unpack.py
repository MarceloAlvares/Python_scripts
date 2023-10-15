tupla1 = (1,1,1)
lista2 = [2,2,2]

def soma(x,y,z):
    return x+y+z

def soma_n(*numeros):
    soma = 0
    for soma in numeros:
        soma += soma
    return soma

# Modo normal passando os 3 parametros posicionais da funcao soma.
print(soma(1,1,1))

# Modo Unpacking sera extraido os valores da tupla e da lista para funcao soma.
print(soma(*tupla1))
print(soma(*lista2))


# Modo Packing onde ele recebe os valores avulsos posicionais e carrega dentro uma tupla
#   da funcao para executar o algoritmo de soma.

print(soma_n(1,2,3))


tupla1 = (1,2,3)
lista2 = [1,2,3]

# Funcao soma limitada com arametros posicionais
def soma(x,y,z):
    return x+y+z

# Funcao soma com * para packing ou unpacking
def soma_n(*numeros):
    somaf = 0
    print(type(numeros)) # mesmo passando lista ele sempre converte para tupla
    for somaf in numeros:
        somaf += somaf
    return somaf

# Modo normal passando os 3 parametros posicionais da funcao soma.
print(soma(1,2,3))

# Modo Unpacking sera extraido os valores da tupla e da lista para  as funcoes de soma.
print(soma(*tupla1))
print(soma_n(*tupla1))

print(soma(*lista2))
print(soma_n(*lista2))

# Modo Packing onde ele recebe os valores avulsos posicionais e carrega dentro uma tupla
# interna dentro funcao para executar o algoritmo de soma.

print(soma_n(1,2,3))




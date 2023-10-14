
# # Lógica utilizando generator para varrer um dicionario
# def get_tipo_dia(dia):
#     dicionario = {
#         (1, 7): "Fim de semana",
#         tuple(range(2, 7)): "Dia util"
#     }

#     generator = (valores for chaves, valores in dicionario.items() if dia in chaves)
    
#     return next(generator, "Dia fora da faixa") # Caso o valor seja nulo (nao encontrado) retorna outra msg, recurso existente somente no generator.

# for dias in range(0,9):
#     resultado = get_tipo_dia(dias)
#     print(resultado)

# =======================================================================================
# Lógica dict comprehension para varrer um dicionario
def get_tipo_diadict(dia):
    dicionario = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "Dia util"
    }

    dict_comp = {valores for chaves, valores in dicionario.items() if dia in chaves}
    return dict_comp

for dias_d in range(0,9):
    resultado = get_tipo_diadict(dias_d)
    if resultado:
        resultado = str(resultado)
        print(resultado)
    else:
        print("Dia fora da faixa")


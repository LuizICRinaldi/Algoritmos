# Dados
inicio = [0, 2, 5, 6, 8, 11]
fim    = [3, 4, 7, 9, 10, 12]

eventos = 0
if len(fim) == len(inicio):
    eventos = len(fim)
else:
    print("error")
    exit()

inicio_ordenado = list(inicio)
fim_ordenado = list(fim)

indice_original = list(range(eventos))


for i in range(eventos):
    for j in range(0, eventos - i - 1):
        if inicio_ordenado[j] > inicio_ordenado[j + 1] or \
        (inicio_ordenado[j] == inicio_ordenado[j + 1] and fim_ordenado[j] > fim_ordenado[j + 1]):
            inicio_ordenado[j], inicio_ordenado[j + 1] = inicio_ordenado[j + 1], inicio_ordenado[j]
            fim_ordenado[j], fim_ordenado[j + 1] = fim_ordenado[j + 1], fim_ordenado[j]
            indice_original[j], indice_original[j + 1] = indice_original[j + 1], indice_original[j]


print(inicio_ordenado)
print(fim_ordenado)

dp = [0] * (eventos + 1)
next_posicao = [-1] * eventos

for i in range(eventos - 1, -1, -1):
    s_i = inicio_ordenado[i]
    f_i = fim_ordenado[i]
    
    solucao_nao_escolher = dp[i + 1]

    proximo_compativel_posicao = eventos 
    
  
    for j in range(i + 1, eventos):
        s_j = inicio_ordenado[j]
        
        if f_i < s_j:
            proximo_compativel_posicao = j
            break 
            
    solucao_escolher = 1 + dp[proximo_compativel_posicao]
    
    if solucao_escolher >= solucao_nao_escolher:
        dp[i] = solucao_escolher
        next_posicao[i] = proximo_compativel_posicao
    else:
        dp[i] = solucao_nao_escolher
        next_posicao[i] = i + 1


eventosEscolhidos = [] 

i = 0
while i < eventos:
    if next_posicao[i] == i + 1:
        i += 1
    elif next_posicao[i] != -1 and next_posicao[i] != eventos:
        eventosEscolhidos.append(indice_original[i])
        
        i = next_posicao[i]
    else:
        if next_posicao[i] == eventos and dp[i] > 0:
             eventosEscolhidos.append(indice_original[i])
        break
        

print("Eventos escolhidos:")
print(eventosEscolhidos)
for i in eventosEscolhidos:
    print(f"Início={inicio[i]}, Fim={fim[i]}")
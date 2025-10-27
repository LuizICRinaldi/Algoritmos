inicio = [1,6,7,9,18,23,25,30]
fim = [26,15,16,15,24,28,30,34]

eventos = 0
if len(fim) == len(inicio): # Caso seja pedido eventos diferentes, só pra ver se ta certinho os arrays
    eventos = len(fim)
else:
    print("error")

eventosEscolhidos = []

ultimo_fim = -1  

while True:
    menor = None
    posicao = -1

    # utilizando o menor fim de cada vez
    for i in range(eventos):
        if i not in eventosEscolhidos and inicio[i] > ultimo_fim:
            if menor is None or fim[i] < menor:
                menor = fim[i]
                posicao = i

    if posicao == -1:  # não há mais eventos validos
        break

    eventosEscolhidos.append(posicao)
    ultimo_fim = fim[posicao]

print("Eventos escolhidos:")

print(eventosEscolhidos)

for i in eventosEscolhidos:
    print(f"Início={inicio[i]}, Fim={fim[i]}")

inicio = [0, 2, 5, 6, 8, 11]
fim    = [3, 4, 7, 9, 10, 12]

eventos = len(inicio)

# Empacotar eventos
intervalos = [(inicio[i], fim[i], i) for i in range(eventos)]

# 1. ORDENAR POR FIM
intervalos.sort(key=lambda x: x[1])

# Extrair vetores ordenados
starts = [x[0] for x in intervalos]
ends   = [x[1] for x in intervalos]
orig   = [x[2] for x in intervalos]

# 2. PRÉ-CÁLCULO DO PRÓXIMO COMPATÍVEL (BUSCA BINÁRIA)
import bisect
next_compat = []
for i in range(eventos):
    j = bisect.bisect_left(starts, ends[i])
    next_compat.append(j)

# 3. DP
dp = [0] * (eventos + 1)

for i in range(eventos - 1, -1, -1):
    dp[i] = max(1 + dp[next_compat[i]], dp[i+1])

# 4. RECONSTRUÇÃO
esc = []
i = 0
while i < eventos:
    if 1 + dp[next_compat[i]] >= dp[i+1]:
        esc.append(orig[i])
        i = next_compat[i]
    else:
        i += 1

# 5. SAÍDA
esc.sort()
print("Eventos escolhidos:", esc)
for i in esc:
    print(inicio[i], fim[i])
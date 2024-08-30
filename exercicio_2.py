def dif_absoluta(n):
    n.sort()
    dif_menor = float('inf')  
    pares_minimos = []

    for i in range(len(n) - 1):
        dif_agr = abs(n[i] - n[i + 1])
        if dif_agr <= dif_menor:
            dif_menor = dif_agr
            if dif_agr < dif_menor:
                pares_minimos = []  
            pares_minimos.append((n[i], n[i + 1]))
    return pares_minimos

numeros = [4, 2, 1, 7, 5, 10]
pares = dif_absoluta(numeros)
print("Os pares com a menor diferença são:", pares)
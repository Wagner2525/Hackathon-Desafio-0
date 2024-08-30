def dif_absoluta(n, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    n.sort()
    dif_menor = float('inf')  
    par_min = []

    for i in range(len(n) - 1):
        if not allow_duplicates and n[i] == n[i + 1]:
            continue  

        dif_agr = abs(n[i] - n[i + 1])
        if dif_agr <= dif_menor:
            dif_menor = dif_agr
            if dif_agr < dif_menor:
                par_min = []  
            par_min.append((n[i], n[i + 1]))

    if sorted_pairs:
        par_min.sort()
    if unique_pairs:
        par_min = list(set(par_min)) 
    return par_min

numeros = [4, 2, 1, 7, 5, 10]
pares = dif_absoluta(numeros, allow_duplicates=False, sorted_pairs=True, unique_pairs=True)
print("Os pares com a menor diferença são:", pares)
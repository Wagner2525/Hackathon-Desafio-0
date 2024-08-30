def subconjuntos_santo(n):
    r = [[]]

    for i in n:
        sub_nv = []
        for sub in r:
            sub_nv.append(sub + [i])
        r.extend(sub_nv)
    return r

n = [1, 2]
subconjuntos = subconjuntos_santo(n)
print(subconjuntos)
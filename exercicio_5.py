from itertools import combinations
def subconjunto_santo(n, max_size=None, min_size =0, distinct_only=False, sort_subsets=False):
    
    if distinct_only:
        n = list(set(n))
    if sort_subsets:
        n.sort()
    tds_sub = []
    
    for i in range(min_size , (max_size or len(n)) + 1):
        for subconjunto in combinations(n, i):
            tds_sub.append(subconjunto)
    
    if sort_subsets:
        tds_sub.sort()    
    return tds_sub

num = [1, 2, 2, 3]
print(subconjunto_santo(num, max_size=3, min_size =1, distinct_only=True, sort_subsets=True))

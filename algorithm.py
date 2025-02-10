def triangulate_all(nodes):
    m = len(nodes)
    comb = [el for el in combinations([i for i in range(m)], 3)]
    triangel_indices = np.array(comb).reshape((m*(m-1)*(m-2)//6,3))
    return triangel_indices

def amount_of_edges(indices, edges):
    return [sum([set(edge).issubset(set(el)) for edge in edges]) for el in indices]

def area_triangle(a,b,c):
    aa = np.linalg.norm(b-c)
    bb = np.linalg.norm(a-c)
    cc = np.linalg.norm(a-b)
    sp = (aa+bb+cc)/2
    area = np.sqrt(sp * (sp - aa) * (sp - bb) * (sp - cc))
    return abs(area)

def checkagain():
    print('Hmmm')

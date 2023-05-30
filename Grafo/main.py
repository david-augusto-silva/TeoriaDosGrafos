from grafo import *

g = GrafoMatrizAdj()

g.DefinirN(n=3)
g.AdcionarAresta(1, 2)
g.AdcionarAresta(1, 3)
g.AdcionarAresta(2, 3)

print("São arestas de G: ")
for v in range(1, g.n + 1):
    for w in g.N(v):
            print(v, w)
            
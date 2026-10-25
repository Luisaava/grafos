import sys
from grafo import Grafo

inf = float('inf')

def floydwarshall(grafo: Grafo): # nao precisa da matriz pi! só precisa do custo
    nv = grafo.num_vertices
    distancia = [[0 for _ in range(nv)] for _ in range(nv)]
    for u in range(nv):
        for v in range(nv):
            if u != v: # já inicializa com 0's
                distancia[u][v] = inf
                if grafo.haAresta(u+1, v+1):
                    distancia[u][v] = grafo.peso(u+1, v+1)
    for k in range(nv):
        for u in range(nv):
            for v in range(nv):
                if distancia[u][v] > distancia[u][k] + distancia[k][v]:
                    distancia[u][v] = distancia[u][k] + distancia[k][v]
    return distancia
            
if __name__=="__main__":
    if len(sys.argv) == 2:
        args = sys.argv
        arquivo_grafo = args[1]
        grafo = Grafo(arquivo_grafo)
        d = floydwarshall(grafo)
        for i in range(grafo.num_vertices):
            print(i+1, end=':')
            for j in range(grafo.num_vertices-1):
                print(d[i][j], end=',')
            print(d[i][grafo.num_vertices-1])

    else:
        print("Forneça os argumentos no seguinte formato: \n" \
        "python3 A1_5.py nome_grafo")
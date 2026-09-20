import sys
from grafo import Grafo

inf = float('inf')

def floydwarshall(grafo: Grafo):
    nv = grafo.num_vertices
    distancia = [[0 for _ in range(nv)] for _ in range(nv)]
    pi = [[None for _ in range(nv)] for _ in range(nv)]
    for u in range(nv):
        for v in range(nv):
            if u != v: # já inicializa com 0's
                distancia[u][v] = inf
                if grafo.haAresta(u+1, v+1):
                    distancia[u][v] = grafo.peso(u+1, v+1)
                    pi[u][v] = u
    for k in range(nv):
        for u in range(nv):
            for v in range(nv):
                if distancia[u][v] > distancia[u][k] + distancia[k][v]:
                    distancia[u][v] = distancia[u][k] + distancia[k][v]
                    pi[u][v] = pi[k][v]
    return (distancia, pi)

def montacaminho(pi, u, v):
    p = [v+1]
    while u != v:
        v = pi[u][v]
        p.insert(0, v+1)
    return p

            
if __name__=="__main__":
    if len(sys.argv) == 3:
        args = sys.argv
        arquivo_grafo = args[1]
        grafo = Grafo(arquivo_grafo)
        x = args[2]
        d, pi = floydwarshall(grafo)

        for i in range(grafo.num_vertices):
            print(i+1, ':')
            for j in range(grafo.num_vertices):
                print(f"de {i+1} a {j+1}")
                print("custo:", d[i][j])
                print("caminho:", montacaminho(pi, i, j))
                print("------------------------------")
            print("=======================")

    else:
        print("Forneça os argumentos no seguinte formato: \n" \
        "python3 ex4_P1.py nome_grafo indice_x")
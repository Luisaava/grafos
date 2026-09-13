import sys
import heapq
from grafo import Grafo

inf = float('inf')

def updateheap(q, index, newval):
    for i, nq in enumerate(q):
        if index == nq[1]:
            q[i] = (newval, index)
            heapq.heapify(q)
            return q

def dijkstra(grafo, s):
    distancia = [inf] * grafo.num_vertices
    ancestral = [None] * grafo.num_vertices
    conhecido = [False] * grafo.num_vertices
    distancia[s-1] = 0
    q = list(zip(distancia, range(1, grafo.num_vertices+1))) # nodo da heap = (distancia à origem, indice do vértice REAL i.e, de 1 a N)
    heapq.heapify(q) # transforma lista em um heap minimo, sem mudar o tipo
    while not len(q) == 0:
        u = heapq.heappop(q) # (Du, INDEXu)
        ind_u = u[1]
        conhecido[ind_u - 1] = True # indice de u - 1 == indice na lista
        for v in grafo.vizinhos(ind_u):
            if not conhecido[v-1] and distancia[v-1] > distancia[ind_u-1] + grafo.peso(ind_u, v):
                distancia[v-1] = distancia[ind_u-1] + grafo.peso(ind_u, v)
                ancestral[v-1] = ind_u
                q = updateheap(q, v, distancia[v-1])
    return (distancia, ancestral)

if __name__=="__main__":
    if len(sys.argv) == 3:
        args = sys.argv
        arquivo_arvore = args[1]
        s = int(args[2])
        grafo = Grafo(arquivo_arvore)
        d, a = dijkstra(grafo, s)
        for i in range(1, grafo.num_vertices+1):
            caminho = [i]
            v = a[i-1]
            while v is not None:
                caminho.insert(0, v)
                v = a[v-1]
            caminho = ','.join(str(n) for n in caminho)
            print(f"{i}: {caminho}; d={d[i-1]}")


    else:
        print("Forneça os argumentos no seguinte formato: \n" \
        "python3 A1_4.py nome_arvore indice_vertice_inicial")
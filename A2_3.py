import sys
from grafo import Grafo
import random
import heapq

inf = float('inf')

def updateheap(q, index, newval):
    for i, nq in enumerate(q):
        if index == nq[1]:
            q[i] = (newval, index)
            heapq.heapify(q)
            return q

def prim(grafo: Grafo):
    r = 2#random.randint(1, grafo.qtdVertices()) # começa por qualquer vértice
    a = [None] * grafo.qtdVertices()
    k = [inf] * grafo.qtdVertices()
    k[r-1] = 0
    q = list(zip(k, range(1, grafo.qtdVertices() + 1))) # nodo da heap = (custo para pendurar na árvore, indice do vértice REAL i.e, de 1 a N)
    heapq.heapify(q) # transforma lista em um heap minimo, sem mudar o tipo
    while not len(q) == 0:
        u = heapq.heappop(q) # tira o mais barato a ser pendurado na árvore
        ind_u = u[1]
        for v in grafo.vizinhos(ind_u):
            if v in [node[1] for node in q] and grafo.peso(ind_u, v) < k[v-1]: # se algum vizinho pode ser pendurado na árvore, atualiza a chave dele (o custo pra pendurar)
                a[v-1] = ind_u
                k[v-1] = grafo.peso(ind_u, v)
                q = updateheap(q, v, k[v-1])
    return a, sum(k)

if __name__=="__main__":
    if len(sys.argv) == 2:
        args = sys.argv
        arquivo_grafo = args[1]
        grafo = Grafo(arquivo_grafo)
        ancestrais, custo_agm = prim(grafo)
        print(custo_agm)
        string_saida_lista = list()
        for v, ancestral in enumerate(ancestrais):
            if ancestral is not None:
                string_saida_lista.append(f'{v+1}-{ancestral}')
        print(', '.join(string_saida_lista))

    else:
        print("Forneça os argumentos no seguinte formato: \n" \
        "python3 A2_3.py nome_grafo")
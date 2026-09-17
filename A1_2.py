from grafo import Grafo
inf = float('inf')

def busca_largura(grafo:Grafo, s:int) :
    C = {} #conhecido ou nao
    D = {} #distancia ate encontrar v
    A = {} #antecessor ao v

    for v in range(1, grafo.qtdVertices() + 1) :
        C[v] = False
        D[v] = inf
        A[v] = None 

    C[s] = True #vertice de origem tem q ta conhecido ja
    D[s] = 0

    Q = [] #esse aqui vai listar os vertices visitados
    Q.append(s) #enqueue

    while len(Q) > 0:

        u = Q.pop(0) #dequeue

        for v in grafo.vizinhos(u):
            if not C[v]:
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.append(v)

    print(D,A)
    return (D, A)


grafo = Grafo("./arquivos_grafos/instancias/caminho_minimo/fln_pequena.net")
busca_largura(grafo, 3)
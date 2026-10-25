from grafo import Grafo
import sys
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

    return (D, A)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Forneça os argumentos:\n python3 A1_2.py caminho_do_arquivo vertice_inicial")
        sys.exit(1)
        
    arquivo = sys.argv[1] #pega o nome do arquivo
    vertice_inicial = int(sys.argv[2]) #pega o vertice inicial 
    
    grafo = Grafo(arquivo) #tornamos o arquivo um grafo
    D, A = busca_largura(grafo, vertice_inicial) #pega a listagem de distancias e guarda em D
    
    niveis = {} #novo dicionario pra saída sair conforme solicitado
    for vertice, nivel in D.items():
        if nivel != inf:
            if nivel not in niveis:
                niveis[nivel] = []
            niveis[nivel].append(vertice)
            
    for nivel in sorted(niveis.keys()):
        lista_vertices = ",".join(map(str, niveis[nivel]))
        print(f"{nivel}: {lista_vertices}")
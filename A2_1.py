import sys
from grafo import Grafo

inf = float('inf')  # constante infinita

def dfs(grafo: Grafo): 
    C = {}  # Se é conhecido ou não
    T = {}  # Tempo de descoberta
    A = {}  # Ancestral de cada vértice
    F = {}  # Tempo de término

    for vertice in grafo.dict_adjacencias: #inicializa os atributos de cada vértice
        C[vertice] = False
        T[vertice] = inf
        A[vertice] = None
        F[vertice] = inf

    tempo = [0] 

    for vertice_ in grafo.dict_adjacencias:
        if not C[vertice_]:
            dfs_visit(grafo, vertice_, C, T, A, F, tempo)

    return C, T, A, F

def dfs_visit(grafo: Grafo, v: int, C: dict, T: dict, A: dict, F: dict, tempo: list): # Primeira DFS!
#vai formando a lista F e visitando os vértices
    C[v] = True
    tempo[0] += 1
    T[v] = tempo[0]

    for u, peso in grafo.dict_adjacencias.get(v, []):
        if not C[u]:
            A[u] = v
            dfs_visit(grafo, u, C, T, A, F, tempo)

    tempo[0] += 1
    F[v] = tempo[0]


def transpor_grafo(grafo: Grafo): #inicializa o grafo_transposto e inverte as arestas
    grafo_transposto = Grafo()
    grafo_transposto.num_vertices = grafo.num_vertices
    grafo_transposto.num_arestas = grafo.num_arestas

    for v in grafo.dict_adjacencias:
        grafo_transposto.dict_adjacencias[v] = []

    for u in grafo.dict_adjacencias:
        for v, peso in grafo.dict_adjacencias[u]:
            grafo_transposto.dict_adjacencias[v].append((u, peso))

    return grafo_transposto


def dfs_adaptado(grafo: Grafo, v: int, C: dict, T: dict, A: dict, F: dict, tempo: list, componente: list): #Segunda DFS (ao grafo transposto)
    C[v] = True
    componente.append(v)  # adiciona vertice à CFC atual
    tempo[0] += 1
    T[v] = tempo[0]

    for u, peso in grafo.dict_adjacencias.get(v, []):
        if not C[u]:
            A[u] = v
            dfs_adaptado(grafo, u, C, T, A, F, tempo, componente) 

    tempo[0] += 1
    F[v] = tempo[0]


def kosaraju(grafo: Grafo):
    # PRIMEIRA DFS para obter os tempos de término (F)
    C, T, A, F = dfs(grafo)

    # Grafo transposto
    grafo_transposto = transpor_grafo(grafo)

    # Ordena os vértices em ordem decrescente do tempo de término F
    vertices_ordenados = sorted(F, key=F.get, reverse=True)

    # SEGUNDA DFS no grafo transposto
    C_t = {u: False for u in grafo_transposto.dict_adjacencias}
    T_t = {u: inf for u in grafo_transposto.dict_adjacencias}
    A_t = {u: None for u in grafo_transposto.dict_adjacencias}
    F_t = {u: inf for u in grafo_transposto.dict_adjacencias}

    componentes_fortemente_conexas = []
    tempo = [0]

    for u in vertices_ordenados:
        if not C_t[u]:
            componente_atual = []
            dfs_adaptado(grafo_transposto, u, C_t, T_t, A_t, F_t, tempo, componente_atual)
            componentes_fortemente_conexas.append(componente_atual)

    return componentes_fortemente_conexas


if __name__ == "__main__":
    if len(sys.argv) > 1:
        caminho_arquivo = sys.argv[1]
    else:
        caminho_arquivo = "./arquivos_grafos/instancias/dirigidos/dirigido2.net"

    grafo = Grafo(caminho_arquivo)
    cfcs = kosaraju(grafo)
    for componente in cfcs:
        print(",".join(map(str, componente)))

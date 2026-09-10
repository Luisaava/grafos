inf = float('inf') # constante infinita

class Grafo:
    def __init__(self, arquivo = None):

        self.num_vertices = 0
        self.num_arestas = 0
        self.rotulos = list() # aqui entra nomes dos vertices, caso tenha
        self.dict_adjacencias = dict() # vertice: [lista de tuplas (vizinho, peso)]
        # ex: {1: [(2, 3), (3, 1)]} -> 1 é vizinho de 2 e a aresta tem peso 3...
        # essas arestas devem se repetir para 2 e 3!

        # se formos acessar a lista de adjacencias com o índice do vértice, é melhor usar dict ou list?
        # ja respondo: usar dict pq nao precisa fazer -1 toda vez, fica melhor de visualizar e a busca é O(1) (!!!)

        # dicionarios foram usados em vez de matriz e afins pois a complexidade é menor

        if arquivo:
            self.ler(arquivo)

    def qtdVertices(self) -> int:
        return self.num_vertices
    
    def qtdArestas(self) -> int:
        return self.num_arestas
    
    def grau(self, v: int) -> int:
        return len(self.dict_adjacencias[v]) # numero de vizinhos do vértice
    
    def rotulo(self, v: int) -> str:
        return self.rotulos[v - 1] # como o v é índice de 1 a n, tem q subtrair 1

    def vizinhos(self, v: int):
        return [edge[0] for edge in self.dict_adjacencias[v]] # itera sobre a lista de arestas do v
    
    def haAresta(self, u: int, v: int) -> bool:
        arestas_u = self.dict_adjacencias[u]
        for aresta in arestas_u: # cada tupla, uma aresta
            if aresta[0] == v: # se o primeiro elemento da tupla for o indice de v, achou
                return True
        return False

    def peso(self, u: int, v: int) -> float:
        arestas_u = self.dict_adjacencias[u]
        for aresta in arestas_u:
            if aresta[0] == v:
                return aresta[1]
        return inf

    def ler(self, arquivo: str):
        lendo_arestas = False
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip().split()
                if linha[0] == "*vertices":
                    self.num_vertices = int(linha[1]) # já descobre o número de vertices
                    for i in range(1, self.num_vertices + 1):
                        self.dict_adjacencias[i] = list() # inicializa a lista de ajacencias
                elif linha[0] == "*edges":
                    lendo_arestas = True
                elif not lendo_arestas: # portanto, lendo vértices
                    self.rotulos.append(' '.join(linha[1:])) # adiciona o rótulo do vértice
                elif lendo_arestas: # portanto, lendo arestas
                    self.num_arestas += 1

                    u = int(linha[0])
                    v = int(linha[1])
                    valor_peso = float(linha[2])

                    self.dict_adjacencias[u].append((v, valor_peso))
                    self.dict_adjacencias[v].append((u, valor_peso)) # aresta para os dois lados
                    # OBS.: dessa forma, a lista de adjacencias fica desordenada
                    # ex.: se o 1 liga com 10 (e não com 2), a chave do 10 é criada antes da chave 2
                    # mas nao muda nada :)
                
if __name__=="__main__":
    # teste = {1: [(1, 2), (3, 4)]}
    # print(2 not in teste)
    grafo = Grafo("./arquivos_grafos/instancias/caminho_minimo/fln_pequena.net")
    # print(grafo.rotulo(1))
    # print(grafo.rotulos)
    # print(grafo.dict_adjacencias[10])
    print(grafo.dict_adjacencias)
    print(grafo.qtdVertices())
    print(grafo.qtdArestas())
    print(grafo.grau(10))
    print(grafo.rotulo(10))
    print(grafo.vizinhos(7))
    print(grafo.haAresta(7, 2))
    print(grafo.haAresta(7, 3))
    print(grafo.peso(7, 3))
    print(grafo.peso(2, 7))
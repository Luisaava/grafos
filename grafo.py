import math

inf = float('inf') # constante infinita

class Grafo:
    def __init__(self, arquivo = None):

        self.quantidade_vertices = 0
        self.quantidade_arestas = 0
        self.rotulos = list() # aqui entra nomes dos vertices, caso tenha
        self.dict_adjacencias = dict() # vertice: [lista de tuplas (vizinho, peso)]
        # ex: {1: [(2, 3), (3, 1)]} -> 1 é vizinho de 2 e a aresta tem peso 3...
        # essas arestas devem se repetir para 2 e 3!

        # se formos acessar a lista de adjacencias com o índice do vértice, é melhor usar dict ou list?
        # ja respondo: usar dict pq nao precisa fazer -1 toda vez, fica melhor de visualizar e a busca é O(1) (!!!)

        # dicionarios foram usados em vez de matriz e afins pois a complexidade é menor

        if arquivo:
            self.ler(arquivo) #TODO

    def qtdVertices(self):
        return self.quantidade_vertices
    
    def qtdArestas(self):
        return self.quantidade_arestas
    
    def grau(self, v: int):
        return len(self.dict_adjacencias[v]) # numero de vizinhos do vértice
    
    def rotulo(self, v: int):
        return self.rotulos[v - 1] # como o v é índice de 1 a n, tem q subtrair 1

    def vizinhos(self, v: int):
        return [edge[0] for edge in self.dict_adjacencias[v]] # itera sobre a lista de arestas do v
    
    def haAresta(self, u: int, v: int):
        arestas_u = self.dict_adjacencias[u]
        for aresta in arestas_u: # cada tupla, uma aresta
            if aresta[0] == v: # se o primeiro elemento da tupla for o indice de v, achou
                return True
        return False

    def peso(self, u: int, v: int):
        arestas_u = self.dict_adjacencias[u]
        for aresta in arestas_u:
            if aresta[0] == v:
                return aresta[1]
        return inf

    def ler(self, arquivo):
        ...

if __name__=="__main__":
    teste = {1: [(1, 2), (3, 4)]}
    # print(teste[1])

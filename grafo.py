import math

class Grafo:
    def __init__(self, arquivo = None):

        self.quantidade_vertices = 0
        self.quantidade_arestas = 0
        self.rotulos = {} #aqui entra nomes dos vertices, caso tenha
        self.vizinhos = {} #conjunto de vizinhos

        ##dicionarios foram usados em vez de matriz e afins pois a complexidade é menor

        if arquivo:
            self.ler(arquivo) #TODO

    def qtdVertices(self) : 
        return self.quantidade_vertices
    
    def qtdArestas(self) : 
        return self.quantidade_arestas
    
    def grau(self, v) : 
        return len(self.vizinhos[v]) #len pega o numero de elementos no conjunto vizinhos
    
    def rotulo(self, v) : 
        return self.rotulos[v]

    def vizinhos(self, v) : 
        return self.vizinhos(v).keys()
    
    def haAresta(self) : 
        return self.quantidade_arestas
    
    def quantVertices(self) : 
        return self.quantidade_arestas
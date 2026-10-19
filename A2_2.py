from grafo import Grafo
import sys

def ot_visit(grafo: Grafo, v: int, C: list[bool], O: list):
    C[v-1] = True
    for u in grafo.vizinhos(v):
        if not C[u-1]:
            C, O = ot_visit(grafo, u, C, O)
    O.insert(0, v)
    return C, O
    
def algo_ot(grafo: Grafo):
    C = [False] * grafo.qtdVertices()
    O = list()
    for v in range(1, grafo.qtdVertices() + 1):
        if not C[v-1]:
            C, O = ot_visit(grafo, v, C, O)
    return O

if __name__=="__main__":
    if len(sys.argv) == 2:
        args = sys.argv
        arquivo_grafo = args[1]
        grafo = Grafo(arquivo_grafo)
        ordem = algo_ot(grafo)
        print(ordem)
        # print([grafo.rotulo(v) for v in ordem])
        print(' , '.join([grafo.rotulo(v) for v in ordem]))

    else:
        print("Forneça os argumentos no seguinte formato: \n" \
        "python3 A2_2.py nome_grafo")
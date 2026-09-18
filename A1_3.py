from grafo import Grafo

def hierholzer (grafo:Grafo):
    if grafo.qtdArestas == 0:
        return(True, {})

    #verifica grau dos vertices!! tem q ser par
    for i in range(1, grafo.num_vertices + 1):
            if grafo.grau(i) % 2 != 0:
                return (False, None)
            
    #


def procura_subciclo(grafo: Grafo, v: int, arestas_nao_visitadas: dict) :
    ciclo = [v] #começa o ciclo com o vertice de origem
    origem = v #salva a origem? pelo o que entendi

    while True:

        if len(arestas_nao_visitadas[v]) == 0: #prossegue se houver aresta nao visitada conectada a CICLO
            return False, None
        
        else:
            #temos que pegar um vertice pra por no ciclo E tirar ele de arestas visitadas
            vertice_visitado = arestas_nao_visitadas[v].pop() 
            arestas_nao_visitadas[vertice_visitado].remove(v)
            #tem que remover da lista dos dois vertices

            v = vertice_visitado

            ciclo.append(v)

        if v == origem:
            break

    i = 0
    while i < len(ciclo) : #aqui a gente vai passr pelos vertices no ciclo e ver se tem aresta faltando visitar
        vertice_no_ciclo = ciclo[i]
        if len(arestas_nao_visitadas[vertice_no_ciclo]) > 0:
            tem_ciclo_ou_nao, ciclo_eba = procura_subciclo(v, arestas_nao_visitadas)

            if tem_ciclo_ou_nao is False:
                return(False, None)

            ciclo = ciclo[:i] + ciclo_eba+ ciclo[i+1:] #fatia o ciclo pra inserir na posicao do vertice_no_ciclo
            
    return (True, ciclo)
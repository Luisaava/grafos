from grafo import Grafo
import sys



def procura_subciclo(v: int, arestas_nao_visitadas: dict) :
    ciclo = [v] #começa o ciclo com o vertice de origem
    origem = v #salva a origem

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
            tem_ciclo_ou_nao, ciclo_ = procura_subciclo(vertice_no_ciclo, arestas_nao_visitadas)

            if tem_ciclo_ou_nao is False:
                return(False, None)

            ciclo = ciclo[:i] + ciclo_+ ciclo[i+1:] #fatia o ciclo pra inserir na posicao do vertice_no_ciclo

            i += len(ciclo_) - 1 #continua a lista a partir do indice do ultimo vertice do subciclo inserido!!
        else:
            i += 1

    return (True, ciclo)


def hierholzer (grafo:Grafo):

    if grafo.qtdArestas() == 0:
        return(True, {})

    #verifica grau dos vertices!! tem q ser par
    for i in range(1, grafo.num_vertices + 1):
            if grafo.grau(i) % 2 != 0:
                return (False, None)
    
    C = {i: grafo.vizinhos(i) for i in range(1, grafo.num_vertices + 1)}

    
    v_inicio = None
    for i in range(1, grafo.num_vertices + 1):
        if len(C[i]) > 0:
            v_inicio = i
            break
            
    sucesso, ciclo = procura_subciclo(v_inicio, C)
    
    if not sucesso:
        return (False, None)

    #verifica grafo desconexo
    for i in range(1, grafo.num_vertices + 1):
        if len(C[i]) > 0:
            return (False, None)

    return (True, ciclo)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Forneça os argumentos:\n python3 A1_3.py caminho_do_arquivo")
        sys.exit(1)
        
    arquivo = sys.argv[1] #pega o nome do arquivo    
    grafo = Grafo(arquivo) #tornamos o arquivo um grafo

    tem_ciclo, C = hierholzer(grafo) #pega o retorno da funcao
    
    if tem_ciclo is True:
        print("1")
        print(",".join([str(v) for v in C]))
    else:
        print("0")
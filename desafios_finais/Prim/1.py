import heapq #implementar da fila de prioridade
import networkx as nx #trabalhar com grafos
import matplotlib.pyplot as plt #desenho do grafo
import json #leitura de arquivos json

#função para encontrar a arvore geradora minima
def prim(G):
    arvore = set()  #conjunto para armazenar as arestas da árvore geradora minima
    visitados = set()  # nos vizitados
    inicio = list(G.keys())[0]  #ponto de partida, de forma aleatoria
    visitados.add(inicio)
    fila = [(peso, inicio, destino) for destino, peso in G[inicio].items()]  #fila de prioridade
    heapq.heapify(fila)

    while fila:
        peso, origem, destino = heapq.heappop(fila)

        #se o destino nao foi visitado, adiciona a aresta a arvore geradora minima
        if destino not in visitados:
            visitados.add(destino)
            arvore.add((origem, destino, peso))

            # Adiciona as arestas do destino aos vizinhos nao visitados a fila de prioridade
            for vizinho, peso_vizinho in G[destino].items():
                heapq.heappush(fila, (peso_vizinho, destino, vizinho))

    return arvore

#criar um grafo resultado com base na arvore geradora mínima
def criar_grafo_resultado(G, arvore):
    grafo_resultado = nx.Graph()

    #arestas com seus pesos ao grafo resultado
    for origem, destino, peso in arvore:
        grafo_resultado.add_edge(origem, destino, weight=peso)

    return grafo_resultado

#desenhar o grafo com a arvore geradora minima destacada
def desenhar_grafo(G, arvore):
    grafo_resultado = criar_grafo_resultado(G, arvore)
    pos = nx.circular_layout(grafo_resultado)  #define a posicao dos nos no layout
    labels = nx.get_edge_attributes(grafo_resultado, 'weight')  #obtem os pesos das arestas
    nx.draw_networkx(grafo_resultado, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')  #desenha o grafo
    nx.draw_networkx_edges(grafo_resultado, pos, edgelist=grafo_resultado.edges(), edge_color='red', width=2)  #destaca as arestas da arvore geradora mínima
    nx.draw_networkx_edge_labels(grafo_resultado, pos, edge_labels=labels)  # adiciona os rotulos das arestas
    plt.show()


with open('graph1.json', 'r') as file:
    grafo_json = json.load(file)


arvore_prim = prim(grafo_json)

#desenhar o grafo 
desenhar_grafo(grafo_json, arvore_prim)

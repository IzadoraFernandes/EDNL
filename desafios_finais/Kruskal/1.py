import networkx as nx #trabalhar com grafos
import matplotlib.pyplot as plt #desenho do grafo
import json #leitura de arquivos json

def kruskal(G):
    arestas = []
    for no_origem, vizinhos in G.items():#obtendo todas as arestas do grafo com seus pesos
        for no_destino, peso in vizinhos.items():
            arestas.append((peso, no_origem, no_destino))

    arestas.sort()#ordenando em ordem crescente as arestas

    arvore = set()#armazenamento das arestas
    conjuntos = {no: {no} for no in G} #inicializando cada no

    for peso, origem, destino in arestas:
        if conjuntos[origem] != conjuntos[destino]: #verificacao se a inclusao nao forma um circulo
            arvore.add((origem, destino, peso))
            conjunto_origem = conjuntos[origem]
            conjunto_destino = conjuntos[destino]
            conjunto_origem.update(conjunto_destino)

            for no in conjunto_destino:#atualizando os conjuntos para analisar a inclusao das arestas
                conjuntos[no] = conjunto_origem

    return arvore

def criar_grafo_resultado(G, arvore):
    grafo_resultado = nx.Graph()

    for origem, destino, peso in arvore:
        grafo_resultado.add_edge(origem, destino, weight=peso)

    return grafo_resultado

def desenhar_grafo(G, arvore):
    grafo_resultado = criar_grafo_resultado(G, arvore)
    pos = nx.circular_layout(grafo_resultado)
    labels = nx.get_edge_attributes(grafo_resultado, 'weight')
    nx.draw_networkx(grafo_resultado, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(grafo_resultado, pos, edgelist=grafo_resultado.edges(), edge_color='red', width=2)
    nx.draw_networkx_edge_labels(grafo_resultado, pos, edge_labels=labels)
    plt.show()

# Leitura do grafo a partir do arquivo JSON
with open('graph1.json', 'r') as file:
    grafo_json = json.load(file)

# Exemplo de uso:
arvore_kruskal = kruskal(grafo_json)

# Desenhar o grafo com a árvore geradora mínima destacada
desenhar_grafo(grafo_json, arvore_kruskal)

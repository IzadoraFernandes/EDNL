import heapq #implementar da fila de prioridade
import networkx as nx #trabalhar com grafos
import matplotlib.pyplot as plt #desenho do grafo
import json #leitura de arquivos json

def dijkstra(G, start): #funcao para encontrar caminho mais curto
    distancias = {node: float('infinity') for node in G}  # inicializando a distancia como infinito
    distancias[start] = 0  # distancia do no de partida
    fila = [(0, start)]  # fila de prioridade para analisar os nos em ordem crescente de distancia
    caminho = {node: None for node in G}  # armazena caminho mais curto

    while fila:
        current_dist, current_node = heapq.heappop(fila)  #no com menor distancia encontrada

        # se a distancia atual for maior, passa para o proximo
        if current_dist > distancias[current_node]:
            continue

        # atualiza as distancias e o caminho para os vizinhos
        for neighbor, weight in G[current_node].items():
            distance = current_dist + weight
            if distance < distancias[neighbor]:
                distancias[neighbor] = distance
                caminho[neighbor] = current_node
                heapq.heappush(fila, (distance, neighbor))

    return distancias, caminho

#criar um grafo com caminho mais curto
def criar_grafo_resultado(G, caminho):
    grafo_resultado = nx.Graph()

    # adiciona as arestas com seus pesos ao grafo resultado
    for node, parent in caminho.items():
        if parent is not None:
            grafo_resultado.add_edge(parent, node, weight=G[parent][node])

    return grafo_resultado

#desenhar o grafo com o caminho mais curto destacado
def desenhar_grafo_com_caminho(G, caminho):
    grafo_resultado = criar_grafo_resultado(G, caminho)
    pos = nx.circular_layout(grafo_resultado)  #define a posicao dos nos no layout
    labels = nx.get_edge_attributes(grafo_resultado, 'weight')  #obtem os pesos das arestas
    nx.draw_networkx(grafo_resultado, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')  #desenha o grafo
    nx.draw_networkx_edges(grafo_resultado, pos, edgelist=grafo_resultado.edges(), edge_color='red', width=2)  #destaca as arestas do caminho
    nx.draw_networkx_edge_labels(grafo_resultado, pos, edge_labels=labels)  # rotulo das arestas
    plt.show()


with open('graph2.json', 'r') as file:
    grafo_json = json.load(file)


inicio_dijkstra = '1'
distancias_dijkstra, caminho_dijkstra = dijkstra(grafo_json, inicio_dijkstra)

#informacoes sobre o caminho mais curto
for node, distancia in distancias_dijkstra.items():
    path = []
    current = node
    while current is not None:
        path.insert(0, current)
        current = caminho_dijkstra[current]
    print(f"Caminho mais curto de {inicio_dijkstra} até {node}: {path}, Peso: {distancia}")

#desenhar o grafo com o caminho mais curto destacado
desenhar_grafo_com_caminho(grafo_json, caminho_dijkstra)
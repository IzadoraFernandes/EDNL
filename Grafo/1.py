import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations


def caixeiro_viajante_grafo(distancias):
    num_cidades = len(distancias)

    # Criação do grafo de forma ponderada
    G = nx.complete_graph(num_cidades) # criação dos grafos com os nós.
    for i in range(num_cidades):
        for j in range(num_cidades):
            if i != j:
                G[i][j]['weight'] = distancias[i][j]

    # Inicializar a melhor solução encontrada até agora
    melhor_caminho = None
    menor_distancia = float('inf')

    # Testar todas as permutações dos nós
    for permutacao in permutations(range(num_cidades)):
        distancia_total = sum(distancias[i][j] for i, j in zip(permutacao, permutacao[1:]))
        distancia_total += distancias[permutacao[-1]][permutacao[0]]  # Voltar à cidade de origem

        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_caminho = list(permutacao) + [permutacao[0]]

    return G, melhor_caminho

# Exemplo de uso
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

solucao_grafo = caixeiro_viajante_grafo(distancias)
print("Caminho ótimo usando grafo:", solucao_grafo)

G, solucao_grafo = caixeiro_viajante_grafo(distancias)

# Desenhar o grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')

# Destacar o caminho ótimo
arestas_destacadas = [(solucao_grafo[i], solucao_grafo[i + 1]) for i in range(len(solucao_grafo) - 1)]
arestas_destacadas.append((solucao_grafo[-1], solucao_grafo[0]))
nx.draw_networkx_edges(G, pos, edgelist=arestas_destacadas, edge_color='red', width=2)

# Exibir a distância total no título
distancia_total = sum(distancias[i][j] for i, j in zip(solucao_grafo, solucao_grafo[1:]))
distancia_total += distancias[solucao_grafo[-1]][solucao_grafo[0]]  # Voltar à cidade de origem
plt.title(f'Caminho ótimo (Distância Total: {distancia_total})')

# Mostrar o gráfico
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
import json
from itertools import permutations

def ler_grafo_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        data = json.load(file)

    G = nx.Graph()

    # Adiciona as arestas ao grafo
    for origem, destinos in data.items():
        for destino, peso in destinos.items():
            G.add_edge(int(origem), int(destino), weight=peso)

    return G

def caixeiro_viajante_grafo(G):
    # Inicializar a melhor solução encontrada até agora
    melhor_caminho = None
    menor_distancia = float('inf')

    # Obter todas as arestas com seus dados
    arestas = list(G.edges(data=True))

    # Obter a lista de todos os nós
    nos = list(G.nodes)

    # Testar todas as permutações dos índices dos nós
    for permutacao_indices in permutations(nos):
        distancia_total = sum(arestas[i][2]['weight'] for i in range(len(permutacao_indices) - 1))
        distancia_total += arestas[permutacao_indices[-1]][2]['weight']  # Voltar ao nó inicial

        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            melhor_caminho = list(permutacao_indices) + [permutacao_indices[0]]

    return G.copy(), melhor_caminho, arestas

# Nome do arquivo JSON contendo a estrutura do grafo
nome_arquivo_json = 'graph1.json'

# Ler o grafo do arquivo JSON
grafo = ler_grafo_do_arquivo(nome_arquivo_json)

# Exemplo de uso
G, solucao_grafo, arestas = caixeiro_viajante_grafo(grafo)

# Desenhar o grafo
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')

# Destacar o caminho ótimo
arestas_destacadas = [(solucao_grafo[i], solucao_grafo[i + 1]) for i in range(len(solucao_grafo) - 1)]
arestas_destacadas.append((solucao_grafo[-1], solucao_grafo[0]))
nx.draw_networkx_edges(G, pos, edgelist=arestas_destacadas, edge_color='red', width=2)

# Exibir a distância total no título
distancia_total = sum(arestas[i][2]['weight'] for i in range(len(solucao_grafo) - 1))
distancia_total += arestas[solucao_grafo[-1]][2]['weight']  # Voltar ao nó inicial
plt.title(f'Caminho ótimo (Distância Total: {distancia_total})')

# Mostrar o gráfico
plt.show()

# Imprimir o melhor caminho no terminal
print("Melhor caminho:", solucao_grafo)

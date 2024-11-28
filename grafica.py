import heapq
import matplotlib.pyplot as plt
import networkx as nx

def primero_el_mejor(grafo, inicio, objetivo):
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))
    cerrados = set()
    predecesores = {}
    caminos = []  # Para almacenar los caminos visitados

    while abiertos:
        _, nodo_actual = heapq.heappop(abiertos)

        if nodo_actual in cerrados:
            continue
        
        cerrados.add(nodo_actual)

        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = predecesores.get(nodo_actual)
            return camino[::-1], caminos  # Retornar el camino y los caminos visitados

        for vecino, peso in grafo.get(nodo_actual, []):
            if vecino not in cerrados:
                heapq.heappush(abiertos, (peso, vecino))
                predecesores[vecino] = nodo_actual
                caminos.append((nodo_actual, vecino))  # Almacenar el camino

    return None, caminos

def graficar_grafo(grafo, camino=None):
    G = nx.Graph()

    # Agregar nodos y aristas al grafo
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos:
            G.add_edge(nodo, vecino, weight=peso)

    # Definir posiciones de los nodos manualmente para uniformidad
    pos = {
        "A": (0, 0),
        "B": (1, 1),
        "C": (1, -1),
        "D": (2, 2),
        "E": (2, 0),
        "F": (2, -2),
        "G": (2.5, -1),
        "H": (3, 0.5),
        "I": (3, -0.5),
        "J": (4, 0.5),
        "K": (4, -1)
    }

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    
    # Dibujar las aristas con sus pesos
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Si hay un camino encontrado, resaltarlo
    if camino:
        camino_edges = [(camino[i], camino[i + 1]) for i in range(len(camino) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=camino_edges, edge_color='red', width=2)

    plt.title("Grafo y Camino Encontrado")
    plt.axis('equal')  # Mantener la proporción de aspecto igual
    plt.show()

# Grafo representado como lista de adyacencia
grafo = {
    "A": [("B", 7), ("C", 6)],
    "B": [("D", 5), ("E", 3)],
    "C": [("F", 9), ("G", 8)],
    "D": [],
    "E": [("H", 1), ("I", 2)],
    "F": [],
    "G": [("K", 0)],
    "H": [("J", 0)],
    "I": [("K", 0)],
    "J": [],
    "K": []
}

# Solicitar al usuario el nodo inicial y objetivo
inicio = input("Introduce el nodo inicial: ").strip()
objetivo = input("Introduce el nodo objetivo: ").strip()

# Ejecutar el algoritmo Primero el Mejor
camino, caminos_visitados = primero_el_mejor(grafo, inicio, objetivo)

# Mostrar el resultado
if camino:
    print("\nCamino encontrado:", " -> ".join(camino))
else:
    print(f"\nNo se encontró un camino entre {inicio} y {objetivo}.")

# Graficar el grafo y el camino encontrado
graficar_grafo(grafo, camino)
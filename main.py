import heapq

def primero_el_mejor(grafo, inicio, objetivo):
    """
    Implementa el algoritmo Primero el Mejor para encontrar el camino más corto en un grafo.

    :param grafo: Diccionario que representa el grafo como lista de adyacencia.
    :param inicio: Nodo de inicio.
    :param objetivo: Nodo objetivo.
    :return: Listado de nodos en el camino más corto o mensaje indicando que no hay solución.
    """
    # Cola de prioridad para los nodos abiertos
    abiertos = []
    heapq.heappush(abiertos, (0, inicio))  # (heurística, nodo)

    cerrados = set()  # Nodos ya explorados
    predecesores = {}  # Para reconstruir el camino

    print("\n--- Inicio del algoritmo ---\n")

    while abiertos:
        # Mostrar el contenido de abiertos y cerrados
        print(f"Abiertos: {[nodo for _, nodo in abiertos]}")
        print(f"Cerrados: {list(cerrados)}\n")

        # Extraer el nodo con menor heurística
        _, nodo_actual = heapq.heappop(abiertos)

        # Si ya fue explorado, continuar con el siguiente
        if nodo_actual in cerrados:
            continue
        
        # Marcar el nodo como cerrado
        cerrados.add(nodo_actual)

        # Si llegamos al objetivo, reconstruir el camino
        if nodo_actual == objetivo:
            print(f"¡Nodo objetivo '{objetivo}' encontrado!")
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = predecesores.get(nodo_actual)
            return camino[::-1]  # Invertimos para obtener el orden correcto

        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo.get(nodo_actual, []):
            if vecino not in cerrados:
                heapq.heappush(abiertos, (peso, vecino))
                predecesores[vecino] = nodo_actual

    # Si no se encuentra el camino, devolver mensaje
    return None


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
camino = primero_el_mejor(grafo, inicio, objetivo)

# Mostrar el resultado
if camino:
    print("\nCamino encontrado:", " -> ".join(camino))
else:
    print(f"\nNo se encontró un camino entre {inicio} y {objetivo}.")